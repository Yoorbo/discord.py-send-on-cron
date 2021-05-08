import discord
import aiocron

client = discord.Client()
token = "YOUR_TOKEN"


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("GAME OF YOUR CHOICE"))
    print('Logged in as {0.user}'.format(client))


@aiocron.crontab('0 */2 * * *')
async def send_on_cron():
    """
    For CRON Editor visit
    https://crontab.guru
    """
    channel = client.get_channel(00000000000)
    await channel.send("MESSAGE")

'''
bot=True For Bot Accounts
bot=False For User Accounts
Use at own risk
'''
client.run(token, bot=False)
