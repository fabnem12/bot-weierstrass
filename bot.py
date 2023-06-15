import asyncio
import nextcord as discord
from nextcord.ext import commands, tasks
from random import randint
from arrow import utcnow

import constantes
from checkFMEL import availability

async def dmChannelUser(user):
    if user.dm_channel is None:
        await user.create_dm()
    return user.dm_channel

updateRate = [100]

def main():
    token = constantes.token

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=";", help_command=None, intents = intents)

    @tasks.loop(minutes = 1.0)
    async def checkAvailability():
        if randint(1, round(updateRate[0])) == 1:
            if availability(constantes.userFMEL, constantes.mdpFMEL):
                await (await dmChannelUser(await bot.fetch_user(constantes.clientId))).send("REGARDE LE SITE DE LA FMEL, IL Y A UN TRUC !!!!")

    @bot.command(name="update_rate")
    async def update_rate(ctx, newRate: int):
        if ctx.author.id == constantes.clientId:
            updateRate[0] = newRate

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)

    @bot.command(name="availability")
    async def check_availability(ctx):
        await ctx.message.add_reaction("👀")
        ret = availability(constantes.userFMEL, constantes.mdpFMEL)
        await ctx.send("Disponibilité de logement FMEL : " + str(ret))

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