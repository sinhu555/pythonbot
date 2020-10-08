import discord
import asyncio

client = discord.Client()
game = discord.Game("ㅋㅋㅋㅋㅋㅋㅋ")

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!봇":
        await message.channel.send("난봇임")
    if message.content == "24":
        await message.channel.send("24시간")

client.run("NzQ5NTYxNjA0OTMyMjM5NDEw.X0txpA.ilZ2735OW-1terCpO8EMThLR1Bg")