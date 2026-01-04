import discord
from discord.ext import commands
import os

# Bot prefix (what you type before commands)
bot = commands.Bot(command_prefix="!")

# Event: when bot is ready
@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}!')

# Test command: !ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Bot is working ✅")

# Run the bot
TOKEN = os.getenv("MTQ1Mjc4MDcxMDY5MDY4OTA0NA.Gvgv5w.8WMztnqA6tvWvl8JWomWkrjqJ1R_Xto9Erdj0E")  # Make sure you put your token in Pella environment variable
bot.run(TOKEN)
