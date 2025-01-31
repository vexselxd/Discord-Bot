import discord
import random
import os
from discord.ext import commands 
from bot_logic import get_air_quality


intents = discord.Intents.default()
intents.members = True 
intents.message_content = True  


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def air(ctx, city: str):
    """
    Comando que obtiene la calidad del aire utilizando el nombre de la ciudad.
    """
    await ctx.send(f"Consultando la calidad del aire en la ciudad: {city}...")

    air_quality_data = get_air_quality(city)

    if 'error' in air_quality_data:
        await ctx.send(f"Error: {air_quality_data['error']}")
    else:
        aqi = air_quality_data.get('aqi', 'No disponible')
        await ctx.send(f"La calidad del aire (AQI) en {city} es: {aqi}")


bot.run("token")




