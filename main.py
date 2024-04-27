import os
import disnake
from disnake.ext import commands


intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, test_guilds=[1229852313649287269])


@bot.event
async def on_ready():
    print("Бот готов!")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


bot.run("token")