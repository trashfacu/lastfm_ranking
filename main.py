import discord
import requests
from discord.ext import commands
from decouple import config

# ENV Variables
API_KEY = config('LASTFM_API_KEY')
BOT_TOKEN = config('BOT_TOKEN')

# URLs
base_url = "http://ws.audioscrobbler.com/2.0/"

# Config bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

users_listfm = []

# Bot joining server
@bot.event
async def on_ready():
    print(f'Bot joined as {bot.user.name}')
    print('server members: ')

    guild = discord.utils.get(bot.guilds, name="facu gang")

    if guild:
        for member in guild.members:
            # Add user info
            user = {
                "discord_name": member.name,
                "lastfm_name": None,
                "scrobbles": 0
            }
            users_listfm.append(user)

            print(member.name)


@bot.command()
async def set_lastfm(ctx, lastfm_username: str):
    user_found = False
    # Search in userlist
    for user in users_listfm:
        if user["discord_name"] == ctx.author.name:
            user["lastfm_name"] = lastfm_username
            user_found = True
            await ctx.send(f"Nombre de usuario de LastFM para {ctx.author.name} establecido como: {lastfm_username}")
            break
    if not user_found:
        await ctx.send("No se encontró tu usuario en la lista")


@bot.command()
async def ranking(ctx):
    user_found = False

    # Filter users who have set their LastFM usernames
    ranked_users = [user for user in users_listfm if user["lastfm_name"]]

    # Get the scrobbles for each user
    for user in ranked_users:
        lastfm_username = user["lastfm_name"]
        user_info_params = {
            "method": "user.getinfo",
            "user": lastfm_username,
            "api_key": API_KEY,
            "format": "json"
        }
        user_info_response = requests.get(base_url, params=user_info_params)
        # Check if it was valid
        if user_info_response.status_code == 200:
            user_info_data = user_info_response.json()
            total_scrobbles = user_info_data.get("user", {}).get("playcount", 0)
            user["scrobbles"] = int(total_scrobbles)
            user_found = True
        else:
            user["scrobbles"] = 0

    # If no LastFM users were found
    if not user_found:
        await ctx.send("Ningún usuario de LastFM encontrado en la lista. Configura tu nombre de usuario de LastFM usando !set_lastfm <nombre_de_usuario_de_LastFM>.")
        return

    # Sorting user list by scrobbles
    sorted_users = sorted(ranked_users, key=lambda x: x["scrobbles"], reverse=True)

    # Creating leaderboard
    leaderboard = "Tabla de Puntuaciones:\n"
    for i, user in enumerate(sorted_users, start=1):
        leaderboard += f"{i}. {user['discord_name']} - Scrobbles: {user['scrobbles']}\n"

    await ctx.send(leaderboard)



@bot.command()
async def help_lastfm(ctx):
    help_message = (
        "!set_lastfm <nombre_de_usuario_de_LastFM>: Establece tu nombre de usuario de LastFM.\n"
        "!ranking: Muestra una tabla de puntuaciones basada en los scrobbles de los usuarios con LastFM configurado.\n"
    )
    
    await ctx.send(help_message)


bot.run(BOT_TOKEN)
