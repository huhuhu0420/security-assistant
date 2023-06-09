# 導入Discord.py模組
import discord
import variebles
from discord.ext import commands
from discord import app_commands
from password_strength import PasswordStats


# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "password", description = "passwd score", guild=discord.Object(id=variebles.SERVERID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction:discord.Integration, passwd:str):
    stats = PasswordStats(passwd)
    await interaction.response.send_message("your password is " + passwd + "\nand your password's strength is: " + str(stats.strength()))

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    await tree.sync(guild=discord.Object(id=variebles.SERVERID))
    print(f"ready --> {client.user}")

@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return
    # 新訊息包含Hello，回覆Hello, world!
    if message.content == "Hello":
        await message.channel.send("Hello, world!")

client.run(variebles.TOKEN)