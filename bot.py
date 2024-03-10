import discord
from discord.ext import commands

#Informações Sensíveis
from dotenv import load_dotenv
import os
load_dotenv('.env')

TOKEN = os.getenv('TOKEN') #Bot token
print(TOKEN)

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready(): #When the bot is ready
  print(f'Logged in as {bot.user} 🔥')

@bot.command(help="It says 'hello' to the bot.")
async def hello(ctx):
  await ctx.send(f'Hello, {ctx.author.global_name}!')

#bot.run(TOKEN) #Turns the bot on