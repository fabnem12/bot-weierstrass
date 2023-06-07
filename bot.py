import asyncio
import nextcord as discord
from nextcord.ext import commands, tasks

import constantes

async def dmChannelUser(user):
    if user.dm_channel is None:
        await user.create_dm()
    return user.dm_channel

def main():
    token = constantes.token

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=";", help_command=None, intents = intents)

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)

    @bot.command(name="hello")
    async def hello(ctx, otherUser: discord.Member):
        await ctx.send(f"hello {ctx.author.mention} https://www.youtube.com/watch?v=tF6LY7lnVFU")
        await (await dmChannelUser(otherUser)).send("Ceci est un test de message privé.")
    
    @bot.command(name="màj")
    async def maj(ctx):
        if ctx.author.id == 619574125622722560:
            from subprocess import Popen, DEVNULL

            await ctx.message.add_reaction("👌")
            Popen(["python3", "maj.py"], stdout = DEVNULL)

    return bot, token

if __name__ == "__main__": #pour lancer le bot
    bot, token = main()

    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(token))
    loop.run_forever()