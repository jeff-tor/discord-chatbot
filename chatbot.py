import os
from dotenv import load_dotenv
load_dotenv()
import discord
import responses
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

class DiscordChatBot:

    async def send_message(self, message, user_message, is_private):

        try:
            response = responses.handle_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(f'an error exception occured:{e}')

    def chat_bot_initialize(self):

        bot = discord.Client(intents=discord.Intents.default())
        print(f'bot is now running {bot.application}')

        @bot.event
        async def on_ready():

            print(f'{bot.user} is now running!')
            guild_count = 0

            # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
            for guild in bot.guilds:

                # PRINT THE SERVER'S ID AND NAME.
                print(f"- {guild.id} (name: {guild.name})")

                # INCREMENTS THE GUILD COUNTER.
                guild_count = guild_count + 1

            # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
            print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

        # EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
        @bot.event
        async def on_message(message):
            # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
            if message.content == "hello":
                # SENDS BACK A MESSAGE TO THE CHANNEL.
                await message.channel.send("hey dirtbag")


        bot.run(token=DISCORD_TOKEN)
