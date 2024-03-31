import os, discord
from discord.ext import commands

from env import env

# from utils.factories import (
#     PersistentTicketView,
#     PersistentTicketButtons,
#     PersistentTicketClosedButtons,
# )


class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="..", intents=discord.Intents.all())

    async def setup_hook(self):
        for i in os.listdir("./src/cogs"):
            for e in os.listdir(f"./src/cogs/{i}"):
                if str(e).endswith(".py"):
                    await client.load_extension(f"cogs.{i}.{e[:-3]}")
                    print(f"✅ Cog loaded\t {i.capitalize()}/{e.capitalize()}")

        # self.add_view(PersistentTicketView())
        # self.add_view(PersistentTicketButtons())
        # self.add_view(PersistentTicketClosedButtons())


intents = discord.Intents.all()
client = MyClient()

client.run(env.token)
