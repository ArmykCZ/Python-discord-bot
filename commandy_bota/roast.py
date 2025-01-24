import discord
from discord.ext import commands
import random

class Roast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Seznam náhodných roastů
    roasts = [
    "Jsi důvod, proč výrobci aut dávají varování před tím, aby řidiči nespoléhali jen na tempomat.",
    "Tvá hlava je tak prázdná, že by si ji Google mohl pronajmout jako datové úložiště.",
    "Kdybys byl software, musel bys být neustále aktualizován… a pořád by to nestačilo.",
    "Jsi tak pomalý, že tě šnek používá jako měřítko rychlosti.",
    "Kdybys měl mozkové buňky, pořád bys měl jen jednu… a ta by byla osamělá.",
    "Jsi jako bug ve videohře – nikdo tě nechce, ale jsi všude.",
    "Tvé IQ má negativní hodnoty – gratuluji, jsi výjimečný!",
    "Tvůj smysl pro humor je tak zastaralý, že si pamatuje dinosaury.",
    "Kdybys byl aplikace, musel by tě Apple odstranit z App Storu kvůli nízké kvalitě.",
    "Tvoje konverzační dovednosti jsou na úrovni porouchaného automatu na kafe.",
    "Jsi tak zbytečný, že kdyby ses ztratil, nikdo by si toho nevšiml.",
    "Kdybys byl barva, byl bys béžový… protože jsi tak nudný.",
    "Tvá logika je tak nefunkční, že by ji i Windows 98 odmítly načíst.",
    "Jsi jako špatný vtip – nikdo tě nechápe, ale všichni se smějí.",
    "Kdybys byl funkce na kalkulačce, byl bys tlačítko 'CE', protože nic neděláš pořádně.",
    "Tvůj talent na cokoli je tak malý, že by se nevešel ani pod mikroskop.",
    "Jsi jako nepřijatelná slohovka – plný chyb a nikdo tě nechce číst.",
    "Tvoje charisma má zápornou hodnotu – odrazuješ i stíny.",
    "Jsi tak otravný, že i komáři se ti vyhýbají.",
    "Tvůj smysl pro orientaci je tak špatný, že by ses ztratil i ve výtahu.",
    "Jsi jako telefon s vybitou baterií – úplně k ničemu.",
    "Kdybys byl emoji, byl bys prostý otazník, protože nikdo nechápe, proč tu jsi.",
    "Tvoje přítomnost je tak slabá, že by ses ztratil v mlze během slunečného dne.",
    "Tvá úroveň kreativity je tak nízká, že Paint by čísla je pro tebe výzvou.",
    "Kdybys byl internetový prohlížeč, jsi Internet Explorer – nepoužitelný a zpomalený.",
    "Tvoje rozhodování je tak špatné, že bys měl být varováním na balení cereálií.",
    "Jsi jako playlist bez oblíbených skladeb – nikdo tě nechce poslouchat.",
    "Tvé argumenty jsou jako dům z karet – stačí fouknout a všechno spadne.",
    "Jsi tak nepozorný, že by sis mohl nechat ujít i vlastní narozeniny.",
    "Kdybys byl zvíře, byl bys lenochod… ale línější.",
    "Tvoje přítomnost v místnosti je tak nevýrazná, že tě i vlastní stín zapomíná následovat.",
    "Jsi jako nekonečný tutoriál – každý čeká, až skončíš."
    ]


    # Command na roast
    @discord.app_commands.command(name='roast', description="Řekni někomu pravdu.")
    async def roast(self, interaction: discord.Interaction, user: discord.User):
        # Náhodně vybere roast ze seznamu
        roast = random.choice(self.roasts)
        # Odešle zprávu s označením uživatele
        await interaction.response.send_message(f"{user.mention}. {roast}")

# Funkce pro přidání cogu do bota
async def setup(bot):
    await bot.add_cog(Roast(bot))
