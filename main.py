import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
click_number = 0
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def click(ctx): 
    global click_number
    click_number += 1
    await ctx.send(f"liczba klikniec {click_number}")

bot.run("token")
