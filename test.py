import discord
import os
import asyncio
from discord.ext import commands  # For better event handling

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # Required for sending messages

# Set up the client with intents
client = discord.Client(intents=intents)

# Event: When the self-bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    CHANNEL_ID = 1408470434768224410  # Replace with your channel ID
    
    try:
        # Fetch the channel by ID
        channel = client.get_channel(CHANNEL_ID)
        if channel is None:
            print(f'Error: Channel with ID {CHANNEL_ID} not found or inaccessible.')
            return
        
        # Verify channel type
        if not isinstance(channel, discord.TextChannel):
            print(f'Error: Channel is not a text channel, type is {channel.type}')
            return
        
        # Send the message
        await channel.send('test')
        print(f'Sent "test" to channel {channel.name}')
        
        # Wait briefly to ensure message is sent
        await asyncio.sleep(1)
        
        # Close the client
        await client.close()
        print('Client closed.')
    except Exception as e:
        print(f'Error sending message: {e}')
        await client.close()

# Retrieve token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    print('Error: DISCORD_TOKEN not found in environment variables.')
else:
    try:
        # Run the self-bot
        client.run(TOKEN)
    except discord.errors.LoginFailure:
        print('Error: Invalid token provided.')
    except Exception as e:
        print(f'Error starting self-bot: {e}')
