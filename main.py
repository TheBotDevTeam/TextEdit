#imports
import sys
import discord
import time

#Files
import KEYS

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
		#you could define the Prefix in the File Keys
		if message.content.startswith(KEYS.PREFIX):
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
				await message.channel.send(content="I sent you a private message with all the orders! If you haven't received anything, please check if you have enabled messages from server members. Also you could find help at https://thebotdev.de/work01.html  https://i.imgur.com/QFtGBSG.png")
				try;
					await message.author.send(embed=discord.Embed(description="***Support***\n**Prefix:**\n-[command]\n**Check if the bot is online**\n-ping \nshows that the bot is online and reads the messages\n**delete messages**\n-clear [ammount]\nDeletes the specified number of messages\n**Create a message**\n-message\nThere is a wizard that will help you to create the message as you like.\n**Bot Info**\n-info\n-----------\nFormatting of the message: *https://thebotdev.de/Markdown.html*\n"))
				except discord.error.Forbidden:
					await message.channel.send(content="Error! i couldnt send you the message per DM so here is the help command for you :)")
					await message.author.send(embed=discord.Embed(description="***Support***\n**Prefix:**\n-[command]\n**Check if the bot is online**\n-ping \nshows that the bot is online and reads the messages\n**delete messages**\n-clear [ammount]\nDeletes the specified number of messages\n**Create a message**\n-message\nThere is a wizard that will help you to create the message as you like.\n**Bot Info**\n-info\n-----------\nFormatting of the message: *https://thebotdev.de/Markdown.html*\n"))
			if invoke == "info":
				await message.channel.send(embed=discord.Embed(color=discord.Color.purple(), description="**Bot by:** *BaseChip*\n**Project:** *TheBotDev*\n**Support:** *[BaseChips support server](https://discord.gg/HD7x2vx)*\n**Bot Invite:** *[INVITE BaseChips Bot](https://discordapp.com/api/oauth2/authorize?client_id=384757717346025472&permissions=67577856&scope=bot)*\n*This is a fork from GitHub from the Bot from BaseChip*"))
			if invoke == "message" and message.author.guild_permissions.administrator == True:
				setup = await message.channel.send(embed=discord.Embed(color=discord.Color.magenta(), description="OK! The setup for creating a message is started. Please send now the color, which should have the border (green/red/magenta/blue/gold) and don't worry about this message and which ones will be written during setup I delete later:) "))

				def checkmsg(m):
					if m.author.id == message.author.id and m.channel.id == message.channel.id:
						return m

				msgwaitfor = await client.wait_for("message", check=checkmsg, timeout=None)
				if msgwaitfor.content != " ":

					if msgwaitfor.content == "green":
						print("Color: Green")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.green(), description="You have chosen the color green. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))
						def checkg(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m
						msg2 = await client.wait_for("message", check=checkg, timeout=None)
						text = await message.channel.send(embed=discord.Embed(color=discord.Color.green(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))

					elif msgwaitfor.content == "red":
						print("Color: Red")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="You have chosen the color red. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))
						def checkr(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m
						msg2 = await client.wait_for("message", check=None, timeout=None)
						text = await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))




					elif msgwaitfor.content == "blue":
						print("Color: Blue")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.blue(),description="You have chosen the color blue. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))
						def checkb(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m
						msg2 = await client.wait_for("message", check=checkb, timeout=None)
						text = await message.channel.send(embed=discord.Embed(color=discord.Color.blue(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))



					elif msgwaitfor.content == "magenta":
						print("Color: Magenta")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.magenta(),description="You have chosen the color magenta. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))

						def checkm(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m
						msg2 = await client.wait_for("message", check=checkm, timeout=None)
						text = await message.channel.send(
							embed=discord.Embed(color=discord.Color.magenta(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))


					elif msgwaitfor.content == "gold":
						print("Color: Gold")
						cg = await message.channel.send(embed=discord.Embed(color=discord.Color.gold(),description="You have chosen the color gold - ok its more yellow, but its called gold. As an example of what the message looks like later, this message has already colored the border. So now please send me the text, which your message should have"))

						def checkgold(m):
							if message.content != None and m.author.id == message.author.id and m.channel.id == message.channel.id:
								return m

						msg2 = await client.wait_for("message", check=checkgold, timeout=None)
						text = await message.channel.send(
							embed=discord.Embed(color=discord.Color.gold(), description=msg2.content))
						try:
							await message.delete()
							await setup.delete()
							await msgwaitfor.delete()
							await cg.delete()
						except discord.error.Forbidden:
							await message.channel.send(embed=discord.Embed(color=discord.Color.red(),description="Oh it looks like that i have to correct myself. I said i am going to delete all messages, but it seems to be that i do not have the permissions to delete messages (manage messages)").set_thumbnail(url="https://thebotdev.de/assets/img/alert.png"))

					else:
						idktc = await message.channel.send(content="Sorry but i dont know this color: "+msgwaitfor.content)
						await asyncio.sleep(20)
						await idktc.delete()



#Log in to Bot
client= MyClient()
client.run(KEYS.TOKEN) #Your Programm does only run if you enter your Prefix in the file KEYS
