import requests
import mashujaahub
import os
from registration.models import Artisan

path = os.path.dirname(mashujaahub.__file__)
fo = open(path+"/.token","r")
bot_token = fo.readline().rstrip('\n')
fo.close()

def telegram_bot_getchatid(phone):
    try:
        obj = Artisan.objects.get(phone=phone)
        return obj.telegramChatId
    except Artisan.DoesNotExist:
        return -1

def telegram_bot_sendtext(bot_message, bot_chatID):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()['ok']
