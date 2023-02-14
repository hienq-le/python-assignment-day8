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
channel_id = bot8_1.get_channel(1070965420137381888)
# Log in
@bot8_1.event
async def on_ready():
	print(str(bot8_1.user)+' successfully logged in!')
# Look for a cat image in the device, send a cat image, then wait 5 minutes and repeat
@bot8_1.slash_command(name="sendcatimageevery5minutes", description="Send a cat image every 5 minutes")
async def send_cat_image_every_5_minutes(self):
	i80 = 0
	while i80 == 0:
		i80 = 0
		try:
			file_to_send = open('20230203_062142_cat.jpg', 'r')
			file_to_send.close()
		except FileNotFoundError:
			await self.respond('Fail to send a cat image!', ephemeral=True)
			print('Fail to send a cat image!')
			time.sleep(300)
			continue
		await self.respond('Sent a cat image\n', file=discord.File('20230203_062142_cat.jpg'), ephemeral=True)
		print('successfully sent a cat image!')
		time.sleep(300)
		continue
# Search cat images with '/searchimage cat' command
@bot8_1.slash_command(name="searchimage", description="Search images with a certain keyword")
async def foo555(self, keyword):
	try:
		if keyword == None or keyword == '\0':
			raise ValueError
	except ValueError:
		await self.respond('Keyword required', ephemeral=True)
		print("Keyword required!")
		return None
	random555 = random.randint(0, 9)
	resource555 = googleapiclient.discovery.build("customsearch", "v1", developerKey = api_key5).cse()
	result555 = resource555.list(q=keyword, cx=search_engine_id5, searchType="image").execute()
	url555 = result555["items"][random555]["link"]
	embed555 = discord.Embed(title="Here\'s your "+keyword+" image:\n")
	embed555.set_image(url=url555)
	await self.respond(embed=embed555, ephemeral=True)
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