"""
Author Michael
Started twooooosday Feb/22/2022
Purpose: to have a bot for various tasks. Mostly what iRoboBot did back on our old IRC server,
plus a few features I might find useful while in chat without wanting to change windows

Version: 1.2.0


OG iRoboBot <3 RIP

xtensive — Feb-28-2022 at 11:57 AM CST
Here's the list output:
I know: start/stop/launched/scores/leaderboard(duckhunt), eightball,
tell, s/find/replace, google, image, seen, powerball, cypher,
crypto, stock, imdb, wiki, weather, random, sl, boobs, version,
rekt, office, homer, chuck, beer, cybor, dwight, pirates, yomama,
BOFH, bored, rules, autism, fc, ap, ralph, ned, rodney, matrix,
michael, princess, confucious, spaceballs, bye.
I also respond to hi, hello, thanks, good job, Is it Friday?, and some more vulgar phrases

"""

import json
import random

import discord
import requests


client = discord.Client()

sad_words = ['sad', 'depressed', 'trump']

starter_encouragements = ["Cheer up!", "Hang in there!", "You can do it!"]

# opening the file in read mode
my_file = open(".env", "r")

# reading the file
data = my_file.read()

my_file.close()
# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.split("\n")
# print(data_into_list[0])


tokenz = data_into_list[0]
owmapi = data_into_list[1]

data_into_list = 'cleared'


# this is a function to return random quotes from a zenquotes website
def get_quote():  # todo rename this function to zenquote but don't break it. we like it <3
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n - " + json_data[0]['a'] + " from <http://zenquotes.io/>"
    return quote


@client.event
async def on_ready():
    print("We have logged in as {0.user} ".format(client))


@client.event
async def on_message(message):  # this is what to do if there is a message appearing in a channel the bot is monitoring
    if message.author == client.user:
        return  # this will ignore the bot when it's speaking, so it doesn't trigger itself

    msg = message.content  # just shortens message.content to msg so I don't have to type it every time.

    if msg.startswith('$hello'):
        await message.channel.send("Hello!")

    if msg.startswith('#inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('@printer'):  # todo, @printer function to print(discord.<variable>)
        await message.channel.send('not functional yet')
        '''
        psudo code
        user says: @printer User_Input
        User_Variable = message - "@printer " 
        print(discord.User_Variable)
        
        purpose: to print variables by name while working on the api
        '''
    if msg.startswith('@weather'):
        print('weather attempt by ' + str(message.author))  # this is going to be for checking the weather at a given location using https://openweathermap.org/api
        # openweathermap.org

        # https://www.simplifiedpython.net/openweathermap-api-python/#Accessing_Data_By_City_Name

        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        # topline = message.content.strip('@roll ')
        city_name = message.content.strip('@weather ')  # todo need to take the text after weather to input into city name. use roller code for reference
        final_url = base_url + "appid=" + owmapi + "&q=" + city_name + "&units=imperial"

        weather_data = requests.get(final_url).json()

        temp = weather_data['main']['temp']

        wind_speed = weather_data['wind']['speed']

        description = weather_data['weather'][0]['description']

        await message.channel.send("\nCurrent Weather Data Of " + city_name + ":\n")
        await message.channel.send("Temperature: " + str(temp) + " degrees fahrenheit")
        await message.channel.send("Wind Speed: " + str(wind_speed) + " MPH")
        await message.channel.send("With " + description)  # todo, need to have this print all in the discord channel instead of to the console

    if msg.startswith('@roll'):  # todo task to pull choose random number from given amount. if no amount given topline defaults to 20
        # print(message.content)
        topline = message.content.strip('@roll ')
        # print(topline)
        if str(topline) == "":
            topline = 20
        # print(random.randrange(int(topline)))
        await message.channel.send("I've rolled a " + str(topline) + " sided die :game_die: Your result is, \n" + str(1 + random.randrange(int(topline))))  # the + 1 is because random starts at 0 and rolling a 6 sided die only gets a max of 5 without this

    if any(word in msg for word in
           sad_words):  # todo, need to parse text so that it reads everything lowercase for this check.
        await message.channel.send(random.choice(starter_encouragements))

    if msg.startswith('@list'):
        await message.channel.send('I know @random, $hello, #inspire')

# todo, @addquote when done as a reply to a message. adds message to list of quotes
# todo @quote responds with a random quote from the list of quotes

# todo, announcement for tweets from certain sources

# todo, @sw <input1> <input2> to search the last few chat messages

# todo, twitter search function
# todo, @google <input> for in chat googleing
# todo, @wiki <input> for in chat wiki searching

client.run(tokenz)  # this actually starts the bot and passes a password to login from the .env file.
# client.run('TOKEN-CONTENTS')  # this is the secret token or whatever
