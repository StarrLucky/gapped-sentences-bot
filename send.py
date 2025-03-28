import requests
import config as config

def send_to_channel(phrase):
    url = f'https://api.telegram.org/bot{config.TGBOT_TOKEN}/sendMessage'
    req = requests.post(url, data = {'chat_id':config.TG_CHAT_ID, 'text':phrase, 'parse_mode':'MarkdownV2'})
    print(req.json())
