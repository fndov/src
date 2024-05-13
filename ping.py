import requests

payload = {
    'content': "**PING** From: Archbtw.com"
}

headers = {
    "authorization": "MTIyMTIyNjk0MjY4MzE1MjU0Nw.G34-Rw.v4NUitlJZqlOWHFETvEokRfWHB24XByK-oaGEo"
}

r = requests.post("https://discord.com/api/v9/channels/1239436153661165582/messages", data=payload, headers=headers)