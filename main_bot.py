import discord
from discord.ext import commands
from projek import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def  password(ctx):
    await ctx.send('BERIKUT PASSWORD UNTUKMU:')
    await ctx.send(gen_pass())

bot.run("MTE5NDI2NDk4NDk3MzIyMjAzOQ.GCu243.-YTLRkaAI9EhcWA0nnnEVD35r375-Ty-TbnaaY")