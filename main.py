import random
import discord
from discord.ext import commands
from cogs.util import store, ready_status

client = commands.Bot(command_prefix=store('config.json', 'pfx', True))

@client.event
async def on_ready():
    await ready_status(client, store('config.json', None, True))
    print("Ready")

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"ERROR: {error}")

@client.event
async def on_message(message):
    if message.author.bot: return
    # if message.channel.id == 0:
    await client.process_commands(message)

@client.command()
async def wakeupmrwest(ctx):
    await ctx.send("<:horny:815833288936914944> WAKE UP MR WEST <:horny:815833288936914944>")

@client.command()
async def quote(ctx):
    await ctx.send(random.choice(store('quotes.json', None, True)))

@client.command()
async def addq(ctx, *, request):
    c = client.get_channel(868667030973321256)
    await c.send(request)
    await ctx.send("ok your request has been sent")

@client.command()
@commands.has_any_role(872954220884688937, 831577493080113193, 792875711676940321, 788912937481273344, 788911513129058304)
async def accept(ctx, *, quote):
    x = store('quotes.json', None, True)
    x.append(quote)
    store('quotes.json', x)
    await ctx.send("ok i appenned that quote yee")

client.run(store('config.json', 'token', True))
