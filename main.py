import os
import asyncio
from boltiotai import openai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from example import example

# Read environment variables safely
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Configure OpenAI
openai.api_key = OPENAI_API_KEY

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN.strip())
dp = Dispatcher()


@dp.message(Command(commands=["start", "help"]))
async def welcome(message: types.Message):
    await message.reply("Hello! I am Mango Chat BOT \n How can I help you?")


@dp.message()
async def gpt(message: types.Message):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": message.text
        }])

    reply_text = response["choices"][0]["message"]["content"].strip()
    await message.reply(reply_text)


async def main():
    # Start Flask keep-alive server
    example()
    # Start Telegram bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
