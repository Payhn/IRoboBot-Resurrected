import discord
import os
import requests
import json
import random

client = discord.Client()


sad_words = ['sad', 'depressed', 'trump']

starter_encouragements = [
    "Cheer up!",
    "Hang in there!",
    "You can do it!"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a'] + " from zenquotes.io"
    return(quote)



'''

this is a thing to read or work with files 

https://www.youtube.com/watch?v=Uh2ebFW8OYM

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents) #prints the contents of the file I'm working with 

print(f.mode)

'''



@client.event
async def on_ready():
        print("We have logged in as {0.user} ".format(client))





###### todo, need to parse text so that it reads everything lowercase. might do that might not

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")

    if message.content.startswith('#inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice (starter_encouragements))


##### todo, need to set a feature so when someone replies to any comment with a #quote command it will add the quote to the list of bot quotes. maybe with a link to the message?


client.run('ODY0NTg3ODk3MTU5ODExMDcz.YO3oOQ.yd63w7lQmaXBvO1bEc0--niR3R4') #this is the secret token or whatever
