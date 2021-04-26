import discord
import dictionary

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$define'):
        await message.channel.send(dictionary.define_word(message.content.split('$define', 1)[1]))

client.run('paste_token_there')
