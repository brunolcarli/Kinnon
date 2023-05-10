import discord
from discord.ext import commands


client = commands.Bot(
    intents=discord.Intents.all(),
    command_prefix='//'
)

 
@client.event
async def on_ready():
    print("READY!")


@client.command()
async def ping(ctx):
    await ctx.send('pong')
