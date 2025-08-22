import discord
import asyncio
import traceback
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        channel_ids = [1346158310235177003]
        friend_channel_id = None
        periodic_message = "Periodic message"
        dm_reply = "Automated response"
        try:
            for cid in channel_ids:
                channel = self.get_channel(cid)
                if channel:
                    print(f"Sending message to channel {cid}")
                    await channel.send(periodic_message)
                else:
                    print(f"Channel {cid} not found")
            dms = [ch for ch in self.private_channels if isinstance(ch, discord.DMChannel)]
            unanswered = []
            for ch in dms:
                if ch.last_message_id:
                    try:
                        last_msg = await ch.fetch_message(ch.last_message_id)
                        if last_msg.author != self.user:
                            unanswered.append((last_msg.created_at, ch))
                    except Exception as e:
                        print(f"Error fetching message in DM {ch.id}: {e}")
            unanswered.sort(key=lambda x: x[0], reverse=True)
            for _, ch in unanswered[:3]:
                print(f"Replying to DM {ch.id}")
                await ch.send(dm_reply)
            if friend_channel_id:
                fchannel = self.get_channel(friend_channel_id)
                if fchannel:
                    if fchannel.last_message_id:
                        try:
                            last_msg = await fchannel.fetch_message(fchannel.last_message_id)
                            user = last_msg.author
                            if user != self.user:
                                print(f"Sending friend request to {user}")
                                await self.http.request(discord.http.Route('PUT', f'/users/@me/relationships/{user.id}'), json={})
                        except Exception as e:
                            print(f"Error sending friend request: {e}")
                            traceback.print_exc()
                    else:
                        print(f"No last message in channel {friend_channel_id}")
                else:
                    print(f"Friend channel {friend_channel_id} not found")
        except Exception as e:
            print(f"Unexpected error: {e}")
            traceback.print_exc()
        finally:
            print("Closing client")
            await self.close()

client = MyClient(intents=discord.Intents.default())
# Retrieve token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable not set")
client.run(TOKEN)
