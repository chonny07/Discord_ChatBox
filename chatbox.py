import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print("Here is the bot")

@bot.command()
async def hello(ctx):
    await ctx.send('Hello chonny')

bot.run('<API token>')