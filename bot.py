
import requests

import discord 

from discord.ext import commands

import json



#client = discord.Client()
# creating a connextion between Adiscord and discord bot 
client = commands.Bot(command_prefix = '!')

@client.event 
async def on_ready():
    print('Bot is ready !')

@client.event
async def on_member_join(member):
    print(f'{member} has joined this server.' )


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def ping2(ctx):
    await ctx.send(f'{round(client.latency*100)} ms')



@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit = amount)


@client.listen('on_message')
async def on_message(message):
    if (message.content.startswith('dog')):
        #response objects is given to you
        request = requests.get('https://some-random-api.ml/img/dog')
        json_dog = json.loads(request.text)

        request2 = requests.get('https://some-random-api.ml/facts/dog')
        json_fact = json.loads(request2.text)

        embed = discord.Embed(title = 'A cute dog picture !',Color = discord.Color.blue())
        embed.set_image(url = json_dog["link"])
        embed.set_footer(text =json_fact["fact"])
        await message.channel.send(embed=embed)

client.run('ODc4MDMxMjMzNzMxNDAzODI2.YR7QTw.upWldf_UzB96CxDLdOfUKeLNEmY')
