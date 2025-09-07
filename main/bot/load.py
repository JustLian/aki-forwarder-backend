from main.bot.start import router as start_router
from aiogram import Dispatcher


def load_routers(dp: Dispatcher) -> None:

    dp.include_router(start_router)
