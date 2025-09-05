from main import Config
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties


bot = Bot(
  token=Config.TOKEN,
  default=DefaultBotProperties(parse_mode="HTML")
)