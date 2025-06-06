import aiohttp
import asyncio
from urllib.parse import urlparse, parse_qs
import json
import re
import os
import time


class Session:
    def __init__(self, token):
        self.token = token


async def login(url, token):
    async with aiohttp.ClientSession() as session:
        url = f"{url}api/v1/auth/login"
        headers = {"User-Agent": "CTFer"}
        data = {
            "teamToken": token,
        }

        async with session.post(url, json=data, headers=headers, allow_redirects=False) as response:
            response_data = await response.json()
            token = response_data['data']['authToken']
            return Session(token=token)


async def down(session, json_data):
    cleaned_json_data = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', json_data)

    data = json.loads(cleaned_json_data)
    while not data['data']:
        print("Challenge not ready yet")
        time.sleep(3)
    async with aiohttp.ClientSession() as session:
        for challenge in data['data']:
            files = challenge['files']
            directory = f"{challenge['category']}/{challenge['name']}"
            os.makedirs(directory, exist_ok=True)
            for file_obj in files:
                url = file_obj['url']
                name_of_file = file_obj['name']
                async with session.get(url) as response:
                    file_data = await response.read()
                file_path = os.path.join(directory, name_of_file)
                with open(file_path, 'wb') as f:
                    f.write(file_data)
            print(f"Downloaded {challenge['name']} to {directory}")

async def start(url, token):
    session = await login(url, token)
    headers = {"User-Agent": "Bengsky",
               "Authorization": "Bearer " + session.token}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f"{url}api/v1/challs") as response:
            response_data = await response.json()
            json_str = json.dumps(response_data, indent=4)
            await down(session, json.dumps(response_data))

def main(url):
    url, token = url.split("login?token=")
    asyncio.run(start(url, token))