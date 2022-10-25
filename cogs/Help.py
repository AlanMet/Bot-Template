from turtle import title
import discord
from discord.ext import commands
from discord import app_commands
import random

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #app_commands(slash commands) take up to 24 hours to load into a server
    @app_commands.command(name = 'hilo', description='says hello')
    async def testy(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"I am working! I was made with Discord.py!", ephemeral = True) 

    @commands.command()
    async def hello(self, msg):
        await msg.send("hello")

    #@commands.Cog.listener()
    #async def on_message(self, msg):
        #await msg.channel.send(f"a message was sent in {msg}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            pass
        else:
            if message.content == "fuck you":
                await message.channel.send("no u")



async def setup(client):
    await client.add_cog(Help(client))
