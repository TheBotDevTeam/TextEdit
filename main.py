#imports
import sys
import discord
import time
import aiohttp

#Files
import KEYS

async def sendmsg(color, message, text):
    try:
        await message.channel.send(embed=discord.Embed(color=color, description=text))
    except:
        pass

async def sendmsg2(color, message, text, link):
    try:
        await message.channel.send(embed=discord.Embed(color=color, description=text).set_thumbnail(url=link))
    except:
        pass
class MyClient(discord.Client):
    async def on_ready(self):
        print("Login successful")
        print("A list of all servers where the bot is on:")
        #List of all Servers the Bot is
        insguilds = 0
        for guild in client.guilds:
            print("%s - %s" %(guild.name, guild.id))
            insguilds = insguilds + 1
        print("Guilds: " + str(insguilds))

        #Game Precense
        game = discord.Game(name="-help")
        await client.change_presence(status=discord.Status.online, game=game)

    async def on_message(self, message):
        if message.content.startswith("-"):
            invoke = message.content[1:].split(" ")[0]
            args = message.content.split(" ")[1:]
            if invoke == "ping":
                await message.channel.send(content="Pong!")

            if invoke == "clear" and message.author.guild_permissions.administrator == True:

                try:
                    ammount = int(args[0])+1 if len(args) > 0 else 1
                except:
                    await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="UNKNOWN VALUE"))
                    return
                async for message in message.channel.history(limit=ammount):
                    try:
                        await message.delete()
                    except discord.error.Forbidden:
                        await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="OH it looks like that i do not have the permissions to delete messages here. I am sorry!"))
                        break

            elif invoke=="clear" or invoke=="message" and message.author.guild_permissions.administrator == False:
                notification = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="This command can only use administrators, sorry").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))
                await asyncio.sleep(20)
                await notification.delete()
            if invoke == "help":
                await message.channel.send(content="I sent you a private message with all the orders!")
                try:
                    await message.author.send(embed=discord.Embed(description="***Support***\n**Prefix:**\n-[command]\n**Check if the bot is online**\n-ping \nshows that the bot is online and reads the messages\n**delete messages**\n-clear [ammount]\nDeletes the specified number of messages\n**Create a message**\n-send color|text\n**with images**\n-header color|your text|link to the image\n**Bot Info**\n-info\n-----------\nFormatting of the message: *https://thebotdev.de/Markdown.html*\n"))
                except discord.error.Forbidden:
                    await message.channel.send(content="Error! i couldnt send you the message per DM")
            if invoke == "info":
                await message.channel.send(embed=discord.Embed(color=discord.Color.purple(), description="**Bot by:** *BaseChip*\n**Project:** *TheBotDev*\n**Support:** *[BaseChips support server](https://discord.gg/HD7x2vx)*\n**Bot Invite:** *[INVITE BaseChips Bot](https://discordapp.com/api/oauth2/authorize?client_id=384757717346025472&permissions=67577856&scope=bot)*\n*This is a fork from GitHub from the Bot from BaseChip*"))
            if invoke == "message" or invoke=="send" and message.author.guild_permissions.administrator == True and message.author.bot==False:
                try:
                    colo, text = message.content.split("|")
                except:
                    await message.channel.send(content="-send color|your text...")
                color = colo.replace("-send ", "")
                if color=="green":
                    await sendmsg(0x00ff00, message, text)
                elif color=="blue":
                    await sendmsg(0x0000ff, message, text)
                elif color=="red":
                    await sendmsg(0xff0000, message, text)
                elif color=="orange":
                    await sendmsg(0xff8000, message, text)
                elif color=="yellow":
                    await sendmsg(0xffff00, message, text)
                elif color=="aqua":
                    await sendmsg(0x00ffff, message, text)
                elif color=="brown":
                    await sendmsg(0x800000, message, text)
                elif color=="black":
                    await sendmsg(0x000000, message, text)
                else:
                    await message.channel.send(embed=discord.Embed(color=0x00ffff,
                                                                   description="color not found (available colors: green, blue, red, orange, yellow, aqua, brown, black - if you need more colors [join my support server](https://discord.gg/HD7x2vx) and tell it to me)"))
            if invoke=="header" and message.author.guild_permissions.administrator==True and message.author.bot==False:
                try:
                    colo, text, link = message.content.split("|")
                except:
                    await message.channel.send(content="-header color|your text...|link to image")
                color = colo.replace("-header ", "")
                if color == "green":
                    await sendmsg2(0x00ff00, message, text, link)
                elif color == "blue":
                    await sendmsg2(0x0000ff, message, text, link)
                elif color == "red":
                    await sendmsg2(0xff0000, message, text, link)
                elif color == "orange":
                    await sendmsg2(0xff8000, message, text, link)
                elif color == "yellow":
                    await sendmsg2(0xffff00, message, text, link)
                elif color == "aqua":
                    await sendmsg2(0x00ffff, message, text, link)
                elif color == "brown":
                    await sendmsg2(0x800000, message, text, link)
                elif color == "black":
                    await sendmsg2(0x000000, message, text, link)
                else:
                    await message.channel.send(embed=discord.Embed(color=0x00ffff, description="color not found (available colors: green, blue, red, orange, yellow, aqua, brown, black - if you need more colors [join my support server](https://discord.gg/HD7x2vx) and tell it to me)"))
            if invoke=="updates" and message.author.id==333220752117596160:
                await message.channel.send(content="Sende...")
                start = time.time()
                counter = 0
                for guild in client.guilds:
                    if counter >= 10:
                        try:
                            await guild.owner.send(content="Hey,\n sorry to bother you, but I am writing to you, because I am on your server `%s` and I was updated, so now I work differently (the message command has been completely revised) and finally you can create messages with an image (-header). For more infos please join my support server (-info);) P.S sorry if you get the message more then one time " % (guild.name))
                        except:
                            pass
                    counter = counter + 1
                    print(counter)
                ende = time.time()
                ins = ende - start
                await message.channel.send(content="fertig - in %s" % (str(ins)))

    async def on_guild_join(self, guild):
        headers = {
            'Authorization': '123456789'}
        data = {'server_count': len(client.guilds)}
        api_url = 'https://discordbots.org/api/bots/384757717346025472/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)

    async def on_guild_remove(self, guild):
        headers = {
            'Authorization': '123456789'}
        data = {'server_count': len(client.guilds)}
        api_url = 'https://discordbots.org/api/bots/384757717346025472/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)

#Log in to Bot
client= MyClient()
client.run(KEYS.TOKEN) #Your Programm does only run if you enter your Prefix in the file KEYS
