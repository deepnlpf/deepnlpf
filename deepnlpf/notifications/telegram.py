# -*- coding: utf-8 -*-

'''
    Date: 02/11/2018
   
              https://core.telegram.org/bots
    Tutorial: https://www.marcodena.it/blog/telegram-logging-handler-for-python-java-bash/
'''

import deepnlpf.config.notification as setting
import requests


class Telegram(object):

    def __init__(self):
        pass

    def send_message(self, message):
        payload = {
            'chat_id': setting.TELEGRAM['CHAT_ID'],
            'text': message,
            'parse_mode': 'HTML'
            }

        if setting.TELEGRAM['SEND_MSG']:
            return requests.post("https://api.telegram.org/bot{token}/sendMessage".format(token=setting.TELEGRAM['TOKEN']), data=payload).content