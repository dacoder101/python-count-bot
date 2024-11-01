"""Initializes and runs the bot and commands."""

import os
import discord
from discord.ext import commands
import dotenv

dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    """Print the bot's name and commands when it's ready."""
    print(f"Logged on as {bot.user}")


bot.run(TOKEN)
