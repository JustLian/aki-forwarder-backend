from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from aiogram import Dispatcher

import asyncio
from contextlib import asynccontextmanager

from main import Config
from main.bot.client import bot
from main.bot.load import load_routers

from main.routers.ws import router as ws_router
from main.routers.uploading import router as uploading_router


dp = Dispatcher()
load_routers(dp)


@asynccontextmanager
async def lifespan(app: FastAPI):
    polling_task = asyncio.create_task(dp.start_polling(bot))  # type: ignore

    try:
        yield
    finally:
        await dp.stop_polling()

        if polling_task and not polling_task.done():
            polling_task.cancel()


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
    "https://aki.rian.moe",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Loading routers
app.include_router(ws_router)
app.include_router(uploading_router)


@app.get("/")
async def root():
    return {"message": "Aki-Forwarder Backend"}


if __name__ == "__main__":
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
