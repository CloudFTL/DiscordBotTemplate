# Import Discord Package

import discord

# Client (My Bot)
client = discord.Client()

@client.event
async def on_ready():
    # DO THE HACKER STUFF
    general_channel = client.get_channel(insert general id)

    await general_channel.send('Insert Message)

@client.event
async def on_message(message):
    if message.content == 'Insert Message':
        general_channel = client.get_channel(insert general id)
        await general_channel.send('insert message')

# Run the client on the server
client.run('insert token')