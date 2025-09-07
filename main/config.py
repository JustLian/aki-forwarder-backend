from os import getenv
from dotenv import load_dotenv


load_dotenv()


class Config:
    PORT = int(getenv("PORT", "8000"))
    HOST = getenv("HOST", "0.0.0.0")

    TOKEN = getenv("TOKEN", "token")
