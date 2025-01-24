import discord
from discord.ext import commands

class Ahoj(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="ahoj", description="Řekne ahoj!")
    async def ahoj(self, interaction: discord.Interaction):
        await interaction.response.send_message("Ahoj, světe!")

async def setup(bot):
    await bot.add_cog(Ahoj(bot))
