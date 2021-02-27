import discord
import os
from discord.ext import commands
import urllib.request

#client = discord.Client()
client = commands.Bot(command_prefix='--')

# Code for ON READY
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(" ")
    await client.change_presence(activity = discord.Game("Poda Venna"))

# Code for ABOUT BOT
@client.command(name='about')
async def about(context):
  myEmbed = discord.Embed(title="About ARASSHWAN",description="The group with so much power of Swaddy")
  myEmbed.add_field(name="Aswin",value="Vj aalu",inline=False)
  myEmbed.add_field(name="Satney",value="Mani aalu",inline=False)
  myEmbed.add_field(name="Aarthmaseels",value="Tharma aalu",inline=False)
  myEmbed.add_field(name="Keerths",value="badava bashkar aalu",inline=False)
  await context.channel.send(embed=myEmbed)


# Entire Code for Message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

# Code for Commands
    if message.content == "$commands":
      myEmbed = discord.Embed(title="COMMANDS",description="")
      myEmbed.add_field(name="$hello",value="Intro about the bot",inline=False)
      myEmbed.add_field(name="$AB [OBJ Name]",value="Picture of the object",inline=False)
      myEmbed.add_field(name="$hello who is swaddy",value="Swaddy intro B|",inline=False)

      await message.channel.send(embed = myEmbed)

# Code for Intro about bot
    if message.content == "$hello":
      await message.channel.send("I am AstroBot. I was created by the great Lord Wolf Swaddy")

# Code for Image Display
    if message.content.startswith("$AB "):
        res = message.content.replace("$AB ", '')

        #author = message.author.decode('UTF-8')
        print(message.author)
        print("Has requested for "+res)
        print(" ")

        res = res.replace(" ","+")

        #await message.channel.send(file=discord.File('NGC_1491.jpg'))

        URL = "https://archive.stsci.edu/cgi-bin/dss_form?target="+res+"&resolver=SIMBAD"

        #print(URL)

        contents = urllib.request.urlopen(URL).read()
        sub = "<input name=r value="
        contentss = contents.decode('UTF-8')
        start = contentss.find(sub) + 21
        con = contentss[start:]
        ra = con.partition('\"')[0]

        sub = "<input name=d value="
        contentss = contents.decode('UTF-8')
        start = contentss.find(sub) + 21
        con = contentss[start:]
        dec = con.partition('\"')[0]

        #print(ra)
        #print(dec)

        ra = ra.replace(" ","+")
        dec = dec.replace(" ","+")
        if(dec[0] == '+'):
          url = "https://archive.stsci.edu/cgi-bin/dss_search?v=poss2ukstu_red&r=" + ra + "&d=%2B" + dec + "&e=J2000&h=15.0&w=15.0&f=gif&c=none&fov=NONE&v3="
        else:
          url = "https://archive.stsci.edu/cgi-bin/dss_search?v=poss2ukstu_red&r=" + ra + "&d=" + dec + "&e=J2000&h=15.0&w=15.0&f=gif&c=none&fov=NONE&v3="

        #print(url)

        await message.channel.send("Getting the images from DSS. Will take some time LOL")
        await message.channel.send(url)

# Code for Swaddy INTRO
    if message.content == "$hello who is swaddy":
      await message.channel.send("The Lord Quantum Wolf is Swaddy")

# Code for Checking Status
    if message.content == "$check":
      await message.channel.send("AstroBot on standby")

# Code for DM's
    if message.content == "$send a DM":
      await message.author.send("This is a DM. Hi User BOOMER")

# Code for Command await
    await client.process_commands(message)

client.run("ODE0MDMyMDQxMDI4MzU0MDY4.YDX8ag.BlH6GEsXvYruZG1vcxEYvVW60jY")
