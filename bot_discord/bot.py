import discord
import requests
import json
import wikipedia


def get_info(search):
    result = wikipedia.summary(search, sentences=2)
    return result
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        elif message.content.startswith('$teste'):
            await message.channel.send('estou funcionando')
        elif message.content.startswith('$info'):
            search_term = message.content[len('$info '):].strip()
            if search_term:
                await message.channel.send(get_info(search_term))
            else:
                await message.channel.send('Por favor, forneça um termo de pesquisa após o comando $info.')
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('token here') # Replace with your own token