# Day 8 - Discord bot about a cat image
import discord, time, googleapiclient, googleapiclient.discovery, random, dotenv, logging, os
try:
    abcxyz5 = open("discord_token.env", 'r')
    dotenv.load_dotenv("discord_token.env")
    abcxyz5.close()
except FileNotFoundError:
    print('TOKEN NOT FOUND!')
    exit()
api_key5 = os.environ.get('API_KEY5')
api_key6 = api_key5
search_engine_id5 = os.environ.get('SEARCH_ENGINE_ID5')
search_engine_id6 = search_engine_id5
intents6 = discord.Intents().all()
client6 = discord.Client(intents=intents6)
handler7 = logging.FileHandler(filename='discord_bot.log', encoding='utf-8', mode='w')
bot8_1 = discord.Bot(intents=intents6)
client_id = int(os.environ.get('CLIENT_ID'))
channel_id = int(os.environ.get('CHANNEL_ID'))
# Log in
@bot8_1.event
async def on_ready():
	print(str(bot8_1.user)+' successfully logged in!')
# Look for a cat image in the device, send a cat image, then wait 5 minutes and repeat
@bot8_1.command(description="Send a cat image every 5 minutes")
async def sendcatimageevery5minutes(ctx):
	i80 = 0
	while i80 == 0:
		i80 = 0
		try:
			file_to_send = open('20230203_062142_cat.jpg', 'r')
			file_to_send.close()
		except FileNotFoundError:
			await bot8_1.get_channel(channel_id).send('Fail to send a cat image!')
			print('Fail to send a cat image!')
			time.sleep(300)
			continue
		await bot8_1.get_channel(channel_id).send('Sent a cat image\n', file=discord.File('20230203_062142_cat.jpg'))
		print('successfully sent a cat image!')
		time.sleep(300)
		continue
# Search cat images with '/searchimage cat' command
@bot8_1.command(description="Search images with a certain keyword")
async def searchimage(ctx, keyword):
	try:
		if keyword == None or keyword == '\0':
			raise ValueError
	except ValueError:
		await bot8_1.get_channel(channel_id).send('Keyword required')
		print("Keyword required!")
		return None
	random555 = random.randint(0, 9)
	resource555 = googleapiclient.discovery.build("customsearch", "v1", developerKey = api_key5).cse()
	result555 = resource555.list(q=keyword, cx=search_engine_id5, searchType="image").execute()
	url555 = result555["items"][random555]["link"]
	embed555 = discord.Embed(title="Here\'s your "+keyword+" image:\n")
	embed555.set_image(url=url555)
	await bot8_1.get_channel(channel_id).send(embed=embed555)
try:
	bot8_1.run(os.environ.get('DISCORD_TOKEN'))
except discord.errors.LoginFailure:
	print('Error login failure!')
	exit()
except discord.errors.PrivilegedIntentsRequired:
	print('Missing intents or required permissions!')
	exit()
except discord.errors.Forbidden:
	print('Missing intents or required permissions!')
	exit()
except discord.errors.ConnectionClosed:
	print('Error: Gateway closed!')
	exit()