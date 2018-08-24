# imports
import traceback
from asyncio import sleep

import aiohttp
# Files
from discord import Embed, Color, Game, Forbidden, Message
from discord.ext.commands import Bot, Context, has_permissions, Converter, BadArgument, CommandNotFound, \
    MissingPermissions

import KEYS


class MyClient(Bot):

    # noinspection PyMethodMayBeStatic
    async def on_ready(self):
        print("Login successful")
        print("A list of all servers where the bot is on:")
        # List of all Servers the Bot is
        insguilds = 0
        for guild in client.guilds:
            print("%s - %s" % (guild.name, guild.id))
            insguilds = insguilds + 1
        print("Guilds: " + str(insguilds))

        # Game Precense
        game = Game(name="-help")
        await client.change_presence(activity=game)

    # noinspection PyMethodMayBeStatic
    async def on_guild_join(self, guild):
        headers = {
            'Authorization': '123456789'}
        data = {'server_count': len(client.guilds)}
        api_url = 'https://discordbots.org/api/bots/384757717346025472/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)

    # noinspection PyMethodMayBeStatic
    async def on_guild_remove(self, guild):
        headers = {
            'Authorization': '123456789'}
        data = {'server_count': len(client.guilds)}
        api_url = 'https://discordbots.org/api/bots/384757717346025472/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)


# Log in to Bot
client = MyClient(command_prefix='-')
client.remove_command('help')


@client.command()
async def help(ctx: Context):
    try:
        await ctx.author.send(embed=Embed(
            description="***Support***\n**Prefix:**\n-[command]\n**Check if the bot is online**\n-ping \nshows that "
                        "the bot is online and reads the messages\n**delete messages**\n-clear [ammount]\nDeletes the "
                        "specified number of messages\n**Create a message**\n-send color text\n**with "
                        "images**\n-header color http://image.link your text\n**Bot "
                        "Info**\n-info\n-----------\nFormatting of the message: "
                        "*https://thebotdev.de/Markdown.html*\n"))
    except Forbidden:
        return await ctx.send(content="Error! i couldnt send you the message per DM")
    await ctx.send(content="I sent you a private message with all the orders!")


@client.command()
@has_permissions(administrator=True)
async def clear(ctx: Context, amount: int = 1):
    async for message in ctx.channel.history(limit=amount):
        try:
            await message.delete()
        except Forbidden:
            return await ctx.send(
                embed=Embed(
                    color=Color.red(),
                    description="OH it looks like that i do not have the permissions to delete messages here. I am "
                                "sorry!"))


@client.command()
async def ping(ctx: Context):
    await ctx.send(content="Pong!")


@client.command()
async def info(ctx: Context):
    await ctx.send(
        embed=Embed(
            color=Color.purple(),
            description="**Bot by:** *BaseChip*\n**Project:** *TheBotDev*\n**Support:** *[BaseChips support server]("
                        "https://discord.gg/HD7x2vx)*\n**Bot Invite:** *[INVITE BaseChips Bot]("
                        "https://discordapp.com/api/oauth2/authorize?client_id=384757717346025472&permissions"
                        "=67577856&scope=bot)*\n*This is a fork from GitHub from the Bot from BaseChip*"))


class ColorConverter(Converter):
    async def convert(self, ctx: Context, argument: str):
        try:
            return getattr(Color, argument.lower())()
        except (TypeError, AttributeError):
            pass
        try:
            return Color(int(argument[1:], 16))
        except (TypeError, ValueError):
            raise BadArgument('Use a hex code or a color name from the supported colors')


@client.command(aliases=['image'])
@has_permissions(administrator=True)
async def header(ctx: Context, color: ColorConverter, link, *, text):
    await ctx.send(
        embed=Embed(
            color=color,
            description=text,
        ).set_thumbnail(url=link)
    )


@client.command(aliases=['message'])
@has_permissions(administrator=True)
async def send(ctx: Context, color: ColorConverter, *, text):
    await ctx.send(
        embed=Embed(
            color=color,
            description=text,
        )
    )


async def on_command_error(ctx: Context, exc: BaseException):
    print('command error')
    mes: Message
    if isinstance(exc, CommandNotFound):
        mes = await ctx.send(
            embed=Embed(
                description="Command not found. See `-help`",
                color=Color.red(),
            )
        )
    elif isinstance(exc, BadArgument):
        mes = await ctx.send(
            embed=Embed(
                description=exc.args[0],
                color=Color.red()))
    elif isinstance(exc, MissingPermissions):
        mes = await ctx.send(
            embed=Embed(
                description="You are missing permissions.",
                color=Color.red()
            )
        )
    else:
        mes = await ctx.send(
            embed=Embed(
                description="An exception occurred during the processing of this command. I might be missing "
                            "permissions here, if not, join our support guild(`-info`) ",
                color=Color.red()
            )
        )
        try:
            raise exc
        except:
            traceback.print_exc()
    if mes:
        await sleep(10)
        await mes.delete()


client.on_command_error = on_command_error

if __name__ == '__main__':
    client.run(KEYS.TOKEN)  # Your Programm does only run if you enter your Prefix in the file KEYS
