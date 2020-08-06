import os
import asyncio
import django
import discord
import giphy_client
import math
import random as r
from channels.db import database_sync_to_async
from discord.ext import commands
from discordbotdjango import settings
from dotenv import load_dotenv
from random import randint
from giphy_client.rest import ApiException

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "discordbotdjango.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from profiles.models import Profile
from quotes.models import Quote, QuotesManager


load_dotenv()
D_TOKEN = os.getenv('discord_token')
G_TOKEN = os.getenv('giphy_token')

prefix = "?"
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
api_instance = giphy_client.DefaultApi()

trigger_words = ['pander']

@bot.event
async def on_ready():
    print('--------')

    # initial_extentions = ['cogs.leveling']

    # if __name__ == '__main__':
    #     for extension in initial_extentions:
    #         try:
    #             bot.load_extension(extension)
    #         except Exception as e:
    #             print(f'Failed to load extension {extension}')
                

    print(f'{bot.user.name} has connected to Discord!')
    print(f'userid: {bot.user.id}')
    print('--------')


async def search_gifs(query):
    try:
        response = api_instance.gifs_search_get(G_TOKEN, query, limit=10, rating='g')
        lst = list(response.data)
        gif = r.choices(lst)

        return gif[0].url

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

@bot.event
async def on_member_join(member):
   embed = discord.Embed(colour=0xb0ec94, url="https://discordapp.com", description=f"Welcome to {member.guild}")
   embed.set_thumbnail(url=f"{member.avatar_url}")
   embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
   embed.set_footer(text="We're all so cute!", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

   channel = discord.utils.get(member.guild.channels, name="general")

   await channel.send(content="", embed=embed)

def __init__(self, bot):
    self.bot = bot


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Pander Gif
    gif = await search_gifs('panda')

    if any(word.lower() in message.content.lower() for word in trigger_words):
        await message.channel.send(gif)

    # Nine-Nine Chat
    if message.content == '99!':
        await message.channel.send('NINE-NINE!')

    # Leveling
    profile_instance = Profile.objects.update_or_create(
    disc_uid = message.author.id,
    )
    # Add +2 EXP
    obj, created = Profile.objects.get_or_create(disc_uid=message.author.id)
    obj.exp += 2
    obj.save()
    # Algorithm for leveling
    xp_start = int(obj.exp)
    lvl_start = int (obj.lvl)
    xp_end = math.floor(5 * (lvl_start ^ 2) + 50 * lvl_start + 100)
    if xp_end < xp_start:
        obj.lvl += 1
        obj.exp = 0
        obj.save()
        await message.channel.send(f"{message.author.mention} has leveled up to level {lvl_start +1}.") 

    # Clear backlog to avoid lock ups
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send('Pong')

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command()
async def rank(ctx):
    obj, created = Profile.objects.get_or_create(disc_uid=ctx.message.author.id)
    await ctx.message.channel.send(f"{ctx.message.author.name} is level {obj.lvl}.")

# Bio and Twitch

@bot.command()
async def setup_bio(ctx, *, content:str):
    obj, created = Profile.objects.get_or_create(disc_uid=ctx.message.author.id)
    obj.bio = str(content)
    obj.save()
    await ctx.message.channel.send('Bio has been updated.')

@bot.command()
async def setup_twitch(ctx, *, content:str):
    obj, created = Profile.objects.get_or_create(disc_uid=ctx.message.author.id)
    obj.twitch = str(content)
    obj.save()
    await ctx.message.channel.send('Twitch has been updated.')

@bot.command()
async def bio(ctx, user:discord.User=None):
    if user is not None:
        obj, created = Profile.objects.get_or_create(disc_uid=user.id)
        if obj.bio == '' and obj.twitch == '':
            await ctx.send('That user has no bio.')
        elif obj.bio != '' and obj.twitch == '':
            await ctx.send(f"{user.name} bio: '{str(obj.bio)}'")
        elif obj.bio == '' and obj.twitch != '':
            await ctx.send(f"{user.name} twitch: 'https://twitch.tv/{str(obj.twitch)}'")
        else:
            await ctx.send(f"{user.name} bio: '{str(obj.bio)}' twitch: 'https://twitch.tv/{str(obj.twitch)}' ")
    elif user is None:
        obj, created = Profile.objects.get_or_create(disc_uid=ctx.message.author.id)
        if obj.bio == '' and obj.twitch == '':
            await ctx.send('That user has no bio.')
        elif obj.bio != '' and obj.twitch == '':
            await ctx.send(f"{ctx.message.author.name} bio: '{str(obj.bio)}'")
        elif obj.bio == '' and obj.twitch != '':
            await ctx.send(f"{ctx.message.author.name} twitch: 'https://twitch.tv/{str(obj.twitch)}'")
        else:
            await ctx.send(f"{ctx.message.author.name} bio: '{str(obj.bio)}' twitch: 'https://twitch.tv/{str(obj.twitch)}' ")


# TV Quotes

@bot.command()
async def tv(ctx):
    await ctx.send(Quote.objects.random())

bot.run(D_TOKEN)
