import discord, asyncio, random, os, asyncpg
from discord.ext import commands
import discord.ext.commands
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.members = True
prefixxx = ['m.', 'M.']
bot = commands.Bot(command_prefix=prefixxx, case_insensitive=True, activity=discord.Game(name="m.help"), intents=intents)
load_dotenv()

###########################################################################################################
################################################MAIN_CODE##################################################
###########################################################################################################

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
bot.remove_command('help')

discord.utils.setup_logging()
@bot.event
async def setup_hook() -> None:
    bot.db: asyncpg.Pool = await asyncpg.create_pool(os.getenv('DBURL'))

######################################################
#######################COMMANDS#######################
######################################################

async def main():
    async with bot:
        [await bot.load_extension(f"commando.{file[:-3]}") for file in os.listdir("commando/") if file.endswith(".py")]
        await bot.start(os.getenv('TOKEN'))

asyncio.run(main())