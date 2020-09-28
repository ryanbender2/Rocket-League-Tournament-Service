import discord
from discord import channel
from discord.message import Message

class MyClient(discord.Client):
    TOKEN = ""


    async def on_ready(self) -> None:
        print(f'Ready for service as {self.user}!')


    async def on_message(self, message: Message) -> None:
        """This is the method that gets called when a 
            message is sent in a server where the bot is installed.
            It gets verified, then sent to the handler.

        Args:
            message ([type]): message details
        """
        if self.verify(message):
            self.handle_event(message)


    def handle_event(self, message: Message) -> None:
        """Method where messages get handled. When any message is
            sent in a server where the bot is installed, this method
            will get called.

            example message details:
                message.author -> ryan.bender2#9842
                message.id -> 760234546620399657
                message.channel -> general
                message.content -> yo guys, what's up?
                message.guild.name -> Tournament Bot Testing

        Args:
            message (Message): message details
        """
        if str(message.author) != "Tournament Bot#8806" and message.content == "Bot, send Gabe a message!":
            channel.send("Bro its insane how easy this thing is to get up and running. This is running in Python.")


    def verify(self, message: Message) -> bool:
        """Verify anything that needs to be checked
            before proceding with handling the message.

        Args:
            message (Message): message event

        Returns:
            bool: event is ready to be handled
        """
        if (str(message.guild.name) != "Tournament Bot Testing"):
            return False

        return True



client = MyClient()
client.run(client.TOKEN)
