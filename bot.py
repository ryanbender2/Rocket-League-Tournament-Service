import discord
from discord import channel
from discord.message import Message

class MyClient(discord.Client):
    TOKEN = ""

    async def on_ready(self) -> None:
        print(f'Logged on as {self.user}!')

    async def on_message(self, message) -> None:
        channel = message.channel

        print(message.author)

        if str(message.author) != "Tournament Bot#8806" and message.content == "Bot, send Gabe a message!":
            await channel.send("Bro its insane how easy this thing is to get up and running. This is running in Python.")



client = MyClient()
client.run(client.TOKEN)
