import names
import random
import string
import discord
import datetime
from random import randint
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(command_prefix="*")

token = input('Bot token:')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="*help"))
    print('bot online')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('bro dont type random things pls')

@client.command()
async def nitro(ctx):
    nitro = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.author.send(f'unchecked nitro code, if it is valid dm to MEE6 sucks#0600: {nitro}')
    await ctx.send('Generated an unchecked code, check your DMs')
    print(f'Nitro code > {nitro}')

@client.command()
async def vmware(ctx):
    code = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
    code1 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
    code2 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
    code3 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))    
    await ctx.author.send(f'unchecked vmware key: {code}-{code1}-{code2}-{code3}')
    await ctx.send('Generated a unchecked vmware key, check your DMs')
    print(f'Vmware key > {code}-{code1}-{code2}-{code3}')

@client.command()
async def valid_nitros(ctx):
    embedVar = discord.Embed(title="**VALID CODES**", description="Valid codes generated:1\nClaimed by:kseMziahG#8213", color=0xff000)
    await ctx.send(embed=embedVar)

@client.command()
async def steam(ctx):
    steam = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
    steam2 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
    steam3 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=5))
    await ctx.author.send(f'unchecked steam key: {steam}-{steam2}-{steam3}')
    await ctx.send('Generated a unchecked steam key, check your DMs')
    print(f'Steam key > {steam}-{steam2}-{steam3}')

@client.command()
async def windows(ctx):
    lines = open('F:\keys.txt').read().splitlines()
    myline = random.choice(lines)
    await ctx.send('Check your dms. All keys are valid')
    await ctx.author.send(myline)

@client.command()
async def gplay(ctx):
    gplay = ('').join(random.choices(string.ascii_uppercase + string.digits, k=4))
    gplay2 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=4))
    gplay3 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=4))
    gplay4 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=4))
    gplay5 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=4))
    await ctx.send('Generated a unchecked google play giftcard, check your dms')
    await ctx.author.send(f'Unchecked google play giftcard: {gplay}-{gplay2}-{gplay3}-{gplay4}-{gplay5}')
    print(f'Google play giftcard > {gplay}-{gplay2}-{gplay3}-{gplay4}-{gplay5}')

@client.command()
async def cc(ctx):
    name = names.get_full_name()
    cc = ('').join(random.choices(string.digits, k=2))
    cc2 = ('').join(random.choices(string.digits, k=4))
    cc3 = ('').join(random.choices(string.digits, k=4))
    cc4 = ('').join(random.choices(string.digits, k=4))
    cvv = ('').join(random.choices(string.digits, k=3))
    date = datetime.date(randint(2022,2030), randint(1,12),randint(1,30))
    await ctx.send('Generated a unchecked credit card, check your dms')
    await ctx.author.send(f'credit card number: 43{cc} {cc2} {cc3} {cc4}\ncvv: {cvv}\nFull name: {name}\nExpiry date: {date}')

client.run(''+token)
