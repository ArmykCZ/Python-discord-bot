import discord
from discord.ext import commands
from discord.ui import Button, View

class Kanaly(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="kanál", description="Vytvoří kanál!")
    async def kanál(self, interaction: discord.Interaction):
        # Vytvoření tlačítka
        button = Button(label="Vytvořit kanál", style=discord.ButtonStyle.primary)

        # Funkce pro vytvoření kanálu po kliknutí na tlačítko
        async def button_callback(interaction: discord.Interaction):
            user_name = interaction.user.name

            # Získání kategorie, pokud neexistuje, vytvoříme ji
            category = discord.utils.get(interaction.guild.categories, name="Nové kanály")
            if category is None:
                category = await interaction.guild.create_category("Nové kanály")

            # Vytvoření textového kanálu s názvem uživatele
            new_channel = await interaction.guild.create_text_channel(user_name, category=category)

            # Skrytí kanálu pro všechny uživatele (everyone)
            await new_channel.set_permissions(interaction.guild.default_role, view_channel=False)

            # Přidání oprávnění pro uživatele, který kliknul
            await new_channel.set_permissions(interaction.user, read_messages=True, send_messages=True)

            # Informování uživatele
            await interaction.response.send_message(f"Kanál {user_name} byl vytvořen a zpřístupněn pro tebe!", ephemeral=True)

            # Změna oprávnění pro každý příkaz /kanál
            # Nastavíme "everyone" na "neviditelný" a pro uživatele, který kliknul na tlačítko - přístup
            await new_channel.set_permissions(interaction.guild.default_role, view_channel=False)  # Skrýt kanál pro všechny

            # Nastavení oprávnění pro uživatele, který na tlačítko kliknul
            await new_channel.set_permissions(interaction.user, view_channel=True, read_messages=True, send_messages=True)

        # Přiřazení callback funkce k tlačítku
        button.callback = button_callback

        # Vytvoření a odeslání zprávy s tlačítkem
        view = View()
        view.add_item(button)
        await interaction.response.send_message("Klikni na tlačítko pro vytvoření kanálu!", view=view)

async def setup(bot):
    await bot.add_cog(Kanaly(bot))
