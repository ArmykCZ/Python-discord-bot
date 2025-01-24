import discord
import random
from discord.ext import commands

# Seznam Pokémonů
POKEMON_LIST = [
    "Beedrill", "Dragonair", "Dugtrio", "Electabuzz", "Electrode", "Pidgeotto", 
    "Arcanine", "Charmeleon", "Dewgong", "Dratini", "Farfetch'd", "Growlithe", 
    "Haunter", "Ivysaur", "Jynx", "Kadabra", "Kakuna", "Machoke", "Magikarp", 
    "Magmar", "Nidorino", "Poliwhirl", "Porygon", "Raticate", "Seel", "Wartortle", 
    "Abra", "Bulbasaur", "Caterpie", "Charmander", "Diglett", "Doduo", "Drowzee", 
    "Gastly", "Koffing", "Machop", "Magnemite", "Metapod", "Nidoran♂", "Onix", 
    "Pidgey", "Pikachu", "Poliwag", "Ponyta", "Rattata", "Sandshrew", "Squirtle", 
    "Starmie", "Staryu", "Tangela", "Voltorb", "Vulpix", "Weedle", "Bill (Trainer)", 
    "Computer Search (Trainer)", "Devolution Spray (Trainer)", "Energy Removal (Trainer)", 
    "Full Heal (Trainer)", "Gust of Wind (Trainer)", "Item Finder (Trainer)", "Lass (Trainer)", 
    "Maintenance (Trainer)", "PlusPower (Trainer)", "Pokémon Breeder (Trainer)", "Pokémon Center (Trainer)", 
    "Pokémon Flute (Trainer)", "Pokédex (Trainer)", "Professor Oak (Trainer)", "Scoop Up (Trainer)", 
    "Super Energy Removal (Trainer)", "Switch (Trainer)"
]

# Seznam Holo karet
HOLO_POKEMON_LIST = [
    "Alakazam (Holo)", "Blastoise (Holo)", "Chansey (Holo)", "Charizard (Holo)", 
    "Clefairy (Holo)", "Gyarados (Holo)", "Hitmonchan (Holo)", "Machamp (Holo)", 
    "Magneton (Holo)", "Mewtwo (Holo)", "Nidoking (Holo)", "Ninetales (Holo)", 
    "Poliwrath (Holo)", "Raichu (Holo)", "Venusaur (Holo)", "Zapdos (Holo)"
]

# Seznam energií
POKEMON_ENERGY = [
    "Double Colorless Energy", "Fighting Energy", "Fire Energy", "Grass Energy",
    "Lightning Energy", "Psychic Energy", "Water Energy"
]

KLASIK_POKEMON_LIST = [
    "Beedrill", "Pidgey", "Poliwag", "Rattata", "Diglett", "Machop", "Magnemite", 
    "Seel", "Koffing", "Caterpie", "Poliwhirl", "Metapod", "Pidgeotto", "Raticate", 
    "Tangela", "Staryu", "Wartortle", "Growlithe", "Kadabra", "Machoke",
    "Potion", "Energy Removal", "Super Energy Removal", "Pokémon Center", 
    "Switch", "Pokédex", "Gust of Wind", "Item Finder", "Bill (Trainer)", 
    "Professor Oak"
]

# Funkce pro otevření balíčku
def open_pokemon_pack():
    # Každý balíček obsahuje 8 náhodných Pokémonů (ne Holo)
    return random.sample(POKEMON_LIST, 7)

def energy_pokemon_pack():
    # Každý balíček obsahuje 2 náhodné energie
    return random.sample(POKEMON_ENERGY, 2)

def holo_pokemon_pack():
    # Každý balíček obsahuje 1 Holo kartu
    return random.sample(HOLO_POKEMON_LIST, 1)

def klasik_pokemon_pack():
    # Každý balíček obsahuje 1 Holo kartu
    return random.sample(KLASIK_POKEMON_LIST, 1)

class OpenPack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Slash příkaz pro otevření balíčku
    @discord.app_commands.command(name="open_pack", description="Otevři Pokémon balíček!")
    async def open_pack(self, interaction: discord.Interaction):
        chance = 0.30  # Šance na speciální kartu
        dobra_karta = random.random()  # Generování náhodného čísla pro šanci

        # Otevření balíčku
        pack = open_pokemon_pack()
        energy = energy_pokemon_pack()
        holo = holo_pokemon_pack()
        klasik = klasik_pokemon_pack()

        # Spojení karet a energií do jedné odpovědi
        if dobra_karta < chance:
            response = ("🎁 Otevřel jsi Pokémon balíček! 🎁\n"
                        f"Obsahuje: {', '.join(pack)} a {', '.join(energy)} a poslední kartu kartu: {', '.join(holo)}")
        else:
            response = ("🎁 Otevřel jsi Pokémon balíček! 🎁\n"
                        f"Obsahuje: {', '.join(pack)} a {', '.join(energy)} a poslední kartu: {', '.join(klasik)}")

        await interaction.response.send_message(response)

# Funkce pro přidání cogu do bota
async def setup(bot):
    await bot.add_cog(OpenPack(bot))
