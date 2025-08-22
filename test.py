import discord
import os

# Set up the client for a self-bot (using user account)
client = discord.Client()

# Event: When the self-bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    # Replace CHANNEL_ID with the target channel's ID (integer)
    CHANNEL_ID = 1346158310235177003  # Example: Replace with your channel ID
    
    try:
        # Fetch the channel by ID
        channel = client.get_channel(CHANNEL_ID)
        if channel is None:
            print(f'Error: Channel with ID {CHANNEL_ID} not found or inaccessible.')
            return
        
        # Send the message
        await channel.send('test')
        print(f'Sent "test" to channel {channel.name}')
        
        # Close the client after sending to avoid staying connected
        await client.close()
    except Exception as e:
        print(f'Error sending message: {e}')

# Retrieve token from Codespace secret (environment variable)
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    print('Error: DISCORD_TOKEN not found in environment variables.')
else:
    try:
        # Run the self-bot with bot=False to indicate user account
        client.run(TOKEN, bot=False)
    except discord.errors.LoginFailure:
        print('Error: Invalid token provided.')
    except Exception as e:
        print(f'Error starting self-bot: {e}')
