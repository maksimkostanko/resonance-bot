# main.py
import discord
from discord.ext import commands
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import threading
import uvicorn
import os

TOKEN = "ВАШ_ТОКЕН_БОТА"  # сюда свой токен бота

# ======= Discord bot =======
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

def start_bot():
    bot.run(TOKEN)

# ======= FastAPI endpoint =======
app = FastAPI()

@app.post("/")
async def interactions(req: Request):
    data = await req.json()
    print("Получен запрос от Discord:", data)
    return JSONResponse(content={"type": 1})

def start_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# ======= Запуск одновременно =======
if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    threading.Thread(target=start_api).start()

