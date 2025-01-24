import discord
from discord.ext import commands
from discord.ui import Button, View

class Kanaly(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="kanál", description="Vytvoří kanál!")
    async def kanál(self, interaction: discord.Interaction):

        button = Button(label="Vytvořit kanál", style=discord.ButtonStyle.primary)

        async def button_callback(interaction: discord.Interaction):
            user_name = interaction.user.name

            category = discord.utils.get(interaction.guild.categories, name="Nové kanály")
            if category is None:
                category = await interaction.guild.create_category("Nové kanály")

            new_channel = await interaction.guild.create_text_channel(user_name, category=category)

            await new_channel.set_permissions(interaction.guild.default_role, view_channel=False)

            await new_channel.set_permissions(interaction.user, read_messages=True, send_messages=True)

            await interaction.response.send_message(f"Kanál {user_name} byl vytvořen a zpřístupněn pro tebe!", ephemeral=True)
          
            await new_channel.set_permissions(interaction.guild.default_role, view_channel=False)  

            await new_channel.set_permissions(interaction.user, view_channel=True, read_messages=True, send_messages=True)

        button.callback = button_callback
        
        view = View()
        view.add_item(button)
        await interaction.response.send_message("Klikni na tlačítko pro vytvoření kanálu!", view=view)

async def setup(bot):
    await bot.add_cog(Kanaly(bot))
