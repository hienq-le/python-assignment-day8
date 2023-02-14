# Day 8 - 2nd Flask app, but it's actually a Slack bot about a cat image
import flask, slackeventsapi, slack_sdk, slack_sdk.errors, time, googleapiclient, googleapiclient.discovery, random, logging, dotenv, os
try:
    abcxyz5 = open("slack_bot_ngrok_url.env", 'r')
    dotenv.load_dotenv("slack_bot_ngrok_url.env")
    abcxyz5.close()
except FileNotFoundError:
    print('TOKEN NOT FOUND!')
    exit()
api_key5 = os.environ.get('API_KEY5')
api_key6 = api_key5
ngrok_authtoken = os.environ.get('NGROK_AUTHTOKEN')
ngrok_authtoken2 = ngrok_authtoken
search_engine_id5 = os.environ.get('SEARCH_ENGINE_ID5')
search_engine_id6 = search_engine_id5
app888 = flask.Flask(__name__)
logger6 = logging.getLogger(__name__)
slack_event_adapter888 = slackeventsapi.SlackEventAdapter(os.environ.get('SIGNING_SECRET'), '/slack/events', app888)
bot8_2 = slack_sdk.WebClient(os.environ.get('TOKEN'))
# Redirect
@app888.route('/', methods=['GET', 'POST'])
def welcome():
    try:
        return flask.redirect(os.environ.get('URL')+'/slack/events')
    except Exception as ex0:
        print(ex0)
        return ex0
# Login
@app888.route('/slack/events', methods=['GET', 'POST'])
def login():
    return flask.render_template('index.html')
# Look for a cat image in the device, send a cat image, then wait 5 minutes and repeat
@app888.route('/slack/commands/sendacatimageevery5minutes', methods=['GET', 'POST'])
def send_a_cat_image_in_5_minutes():
    channel8 = flask.request.form.get('channel_id')
    a8 = 0
    while a8 == 0:
        a8 = 0
        try:
            result6 = bot8_2.files_upload_v2(
            file='20230203_062142_cat.jpg',
            channel=channel8,
            initial_comment='Sent a cat image\n',
            )
            logger6.info(result6)
            print('Sent a cat image')
            time.sleep(300)
            continue
        except Exception as e6:
    # You will get a SlackApiError if "ok" is False
            assert e6.response["ok"] is False
    # str like 'invalid_auth', 'channel_not_found'
            assert e6.response["error"]
            print("Got an error: "+str(e6.response['error']))
            time.sleep(300)
            continue
    return flask.render_template('send_a_cat_image_every_5_minutes.html')
        # Search cat images with '/searchimage cat' command
@app888.route('/slack/commands/searchimage', methods=['GET', 'POST'])
def search_image_by_keyword():
    keyword = flask.request.form.get('text')
    channel8 = flask.request.form.get('channel_id')
    try:
        if keyword == None or keyword == '\0':
            raise ValueError
    except ValueError:
        print("Error: keyword required!")
        return flask.render_template('error.html')
    random555 = random.randint(0, 9)
    resource555 = googleapiclient.discovery.build("customsearch", "v1", developerKey = api_key5).cse()
    result555 = resource555.list(q=keyword, cx=search_engine_id5, searchType="image").execute()
    url555 = result555["items"][random555]["link"]
    try:  
        result = bot8_2.chat_postMessage(
        channel=channel8,
        text="Here\'s your "+keyword+ " image:\n"+url555
        )
        print(result)
        return flask.Response('abc.html', url=url555)
    except Exception as e7:
        print("Error: "+str(e7))
        return flask.render_template('error.html')
if __name__ == '__main__':
    app888.run(debug = True, port = 5000)