import requests

payload = {
    'content': "**PING** From: Archbtw.com"
}

headers = {
    "authorization": "MTIyMTIyNjk0MjY4MzE1MjU0Nw.GdhlG9.7o7PwN_9HDwxgE0brEVdG2SNuO0Ao1LCZhR860"
}

r = requests.post("https://discord.com/api/v9/channels/1239436153661165582/messages", data=payload, headers=headers)