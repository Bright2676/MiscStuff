import discord

from discord.ext import commands
from discord.ext.commands import has_permissions

token = "TOKEN HERE"

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot ready!")

@bot.command(name="test")
async def test(ctx):
    await ctx.reply(f"This is a test command!")

bot.run(token)