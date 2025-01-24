import discord
from discord.ext import commands
import commandy_bota  

class MyBot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents, **kwargs):
        super().__init__(command_prefix, intents=intents, **kwargs)
        self.cog_list = ['commandy_bota.open_pack', 'commandy_bota.ahoj', "commandy_bota.kanaly", "commandy_bota.roast"]

    async def setup_hook(self):
        for cog in self.cog_list:
            try:
                cog_name = cog.split('.')[-1]
                await self.load_extension(cog)
                print(f"Successfully installed module {cog_name}")
            except Exception as e:
                print(f"Error loading cog: {cog} - {e}")


intents = discord.Intents.default()
intents.message_content = True
bot = MyBot(command_prefix="/", intents=intents)



@bot.event
async def on_ready():
    if not hasattr(bot, "synced"):
        await bot.tree.sync()
        bot.synced = True
        print("Slash příkazy byly synchronizovány.")
    print(f'Bot je připojen jako {bot.user}')



TOKEN = "Tvuj token"

# Spuštění bota
if TOKEN:
    bot.run(TOKEN)
else:
    print("Token nebyl nalezen! Zkontrolujte kód.")



