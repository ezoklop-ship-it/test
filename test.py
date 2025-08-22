import asyncio
import os
from dotenv import load_dotenv
from ro_py.client import Client  # Install with: pip install ro-py

# Load environment variables (for secure token storage)
load_dotenv()

# Retrieve .ROBLOSECURITY token from environment variable
# To get your token: Log in to Roblox in a browser, inspect cookies, copy .ROBLOSECURITY value
TOKEN = os.getenv('ROBLOX_TOKEN')

if TOKEN is None:
    print('Error: ROBLOX_TOKEN not found in environment variables.')
else:
    # Create the client with the token for authentication
    client = Client(TOKEN)

    async def main():
        try:
            # Get the authenticated user (yourself) to verify login
            me = await client.get_authenticated_user()
            print(f'Logged in as {me.name} (ID: {me.id})')
            
            # Example: Replace with the target user's ID (integer) or username (string)
            TARGET_USER_ID = 3  # Example: Roblox's user ID; use a real one for testing
            
            # Fetch the target user
            target_user = await client.get_user(TARGET_USER_ID)
            if target_user is None:
                print(f'Error: User with ID {TARGET_USER_ID} not found.')
                return
            
            # Follow the user
            await target_user.follow()
            print(f'Successfully followed {target_user.name}')
            
            # Send a friend request
            await target_user.send_friend_request()
            print(f'Sent friend request to {target_user.name}')
            
        except Exception as e:
            print(f'Error: {e}')

    # Run the async main function
    asyncio.run(main())
