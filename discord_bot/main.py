from dotenv import load_dotenv
load_dotenv()

import os

TOKEN = os.environ.get("DISCORD_TOKEN")

import discord
from discord.ext import commands

import random

from password_gen import sifre_olustur

permissions = discord.Intents.all()
permissions.message_content = True

bot = commands.Bot(command_prefix="!", intents=permissions)

@bot.event
async def on_ready():
    print(f"The bluetooth device is ready to pair.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("ty"):
        await message.channel.send(f"No problem c:")
    if message.content.startswith("i feel sad"):
        await message.channel.send(f"Sorry to hear that, hope you feel better soon c:")
    if message.content.startswith("what"):
        await message.channel.send(f"what?")
    if message.content.startswith("i hate you"):
        await message.channel.send(f"Aw man :c")
    if message.content.startswith("hello"):
        await message.channel.send(f"hello there, I am a {bot.user.name}, epic.")
    if message.content.startswith("merhaba"):
        await message.channel.send(f"merhaba, ben {bot.user.name}")
    await bot.process_commands(message)

@bot.command("rolladie")
async def roll(ctx):
    number = random.randint(1,6)
    await ctx.send(f"Your number is {number} which is a number :O")

@bot.command("flipacoin")
async def flip(ctx):
    side = random.randint(1,2)
    await ctx.send(f"It landed on {side}. 1 is heads, 2 is tails. Im too lazy to figure out how to it with text.")

# @bot.command("sum")
# async def sum(ctx, num1, num2):
#     sum = int(num1) + int(num2)
#     await ctx.send(str(sum))

@bot.command("sum")
async def sum(ctx, *nums):
    total = 0
    for num in nums:
        total += int(num)
    await ctx.send(str(total))

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command("password", description='For when youre too lazy to make your own password :P')
async def gen_password(ctx, count):
    password = sifre_olustur(int(count))
    await ctx.send(f"Your password that I, The Great {bot.user.name} epically created is: {password}")

bot.run(TOKEN)