import discord
from discord import app_commands
from discord.ext import commands

# Your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@client.tree.command(name="ping", description="Check the bot's latency")
async def ping_command(interaction: discord.Interaction):
    latency = client.latency * 1000  # Convert to milliseconds
    await interaction.response.send_message(f'🏓 Pong! Latency is {latency:.2f}ms')

client.run(BOT_TOKEN)
