import discord
from discord.ext import commands 
from bot_logic import gen_pass, game, currency, gen_emoji, flip_coin
#import os

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True  


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_guild_join(guild):
    print(f"Me uní al servidor: {guild.name}")
    channel = next(
        (chan for chan in guild.text_channels if chan.permissions_for(guild.me).read_messages),
        None
    )
    if channel:
        await channel.send(f"¡Hola a todos en **{guild.name}**! 🙌\n"
                           "Gracias por invitarme. Usa `$help` para ver todos mis comandos.")




@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, password_count = 20):
    await ctx.send(gen_pass(password_count))

@bot.command()
async def ball (ctx):
    await ctx.send(game())

@bot.command()
async def currency(ctx):
    await ctx.send(currency())

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

token = "token" 

if token:
    bot.run(token)
else:
    print("Error: No se encontró el token.")
