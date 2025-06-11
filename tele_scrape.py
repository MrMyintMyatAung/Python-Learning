from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import os
from colorama import Fore, Back, Style # add some color to the terminal print

app_api_id = '18161678'
app_api_hash = 'c33ad2f1f12222563d25fddbf7bdd301'

client = TelegramClient('session', app_api_id, app_api_hash)

async def join_channel(client, channel_link):
    try:
        await client(JoinChannelRequest(channel_link))
        print(f"{Fore.CYAN}Joined channel: {channel_link}")
    except Exception as e:
        print(f"Failed to join channel: {e}")

async def get_messages(client, channel, limit=5):
    async for message in client.iter_messages(channel, limit):
        if message.text:
            # Print the message in a structured format
            print(Fore.BLUE + (message.text)) # <--- we addeed stringify to format the messages 
            print(Fore.WHITE + '------------------------------------------------------------------------------------')

async def main():
     # Define the Telegram channel link to monitor (in this case, Durov's channel)
    channel_link = 'https://t.me/Durov'
    await join_channel(client, channel_link)

    await get_messages(client, channel_link)


##async def main():
    # Simple example: send a message to yourself
  ##  await client.send_message('me', 'We are good to go!')

with client:
    client.loop.run_until_complete(main())