import random
import discord
from discord.ext import commands
from cogs.util import store, ready_status

client = commands.Bot(command_prefix=store('config.json', 'pfx', True))

@client.event
async def on_ready():
    guild = client.get_guild(788886124159828009)
    global emojis
    emojis = await guild.fetch_emojis()
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

@client.command(aliases=['q', 'quotes'])
async def quote(ctx):
    await ctx.send(f"{random.choice(store('quotes.json', None, True))} {random.choice(emojis)}")

@client.command(description="shows how many quotes exist")
async def count(ctx):
    await ctx.send(f"there are {len(store('quotes.json', None, True))} quotes recorded")

@client.command()
async def freeishot(ctx):
    await ctx.send("<:horny:815833288936914944> <:horny_2:866447638516858880> <:horny_tongue:827959001311346688>")

@client.command(description="add a quote to the list")
@commands.has_any_role(872954220884688937, 831577493080113193, 792875711676940321, 788912937481273344, 788911513129058304)
async def accept(ctx, *, quote):
    if quote.startswith("\"") or quote.endswith("\""):
        await ctx.send("WTF MAN YUO HAVE QUOTATION MARKS IN YOUR QUOTE REMOVE THEM OR I WILL FUCK YOU IN THE ASS")
        return
    x = store('quotes.json', None, True)
    x.append(quote)
    store('quotes.json', x)
    await ctx.send("👍 added")

client.run(store('config.json', 'token', True))
