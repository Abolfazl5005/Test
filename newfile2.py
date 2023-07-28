from libraryArsein.Arsein import Robot_Rubika
from urllib.request import urlopen
from requests import get
from re import findall
from rubika.encryption import encryption
import time
from rubika.client import Bot
from rubika.tools import Tools

import json

bot = Bot("chfampuoatqwbuualkxeiocboysfakfs")
target="g0DUOEV0688ffafc2d5566572d55ca0c"
sleeped = False
if text.startswith("+"):
	text=msg.get("text")
test_url = 'https://gpt.irateam.ir/api/web.php?apikey=dYU91666028215531nbeb&type=freegpt4&question='+"text"

response = urlopen(test_url)

output_json = json.loads(response.read())
bot.sendMessage(target,output_json["results"]["answer"]+"\n کانال ما : @Id", message_id=msg.get("text"))
