# -*- coding: utf-8 -*-

'''
    Description: Notificações no desktop.
    Date: 01/11/2018
'''

import pathlib
import subprocess as sp
import deepnlpf.config.notification as setting

class Toast(object):

    """
        List emoticons system linux.

        face-angel.png        face-sad.png         stock_smiley-13.png
        face-angry.png        face-sick.png        stock_smiley-15.png
        face-cool.png         face-smile-big.png   stock_smiley-18.png
        face-crying.png       face-smile.png       stock_smiley-1.png
        face-devilish.png     face-smirk.png       stock_smiley-22.png
        face-embarrassed.png  face-surprise.png    stock_smiley-2.png
        face-glasses.png      face-tired.png       stock_smiley-3.png
        face-kiss.png         face-uncertain.png   stock_smiley-4.png
        face-laugh.png        face-wink.png        stock_smiley-5.png
        face-monkey.png       face-worried.png     stock_smiley-6.png
        face-plain.png        stock_smiley-10.png  stock_smiley-7.png
        face-raspberry.png    stock_smiley-11.png  stock_smiley-8.png
    """


    def send_notification(self, icon, title, mensage):
        '''
            Send notification desktop.

            @param 
                icon
                title
                mensage
        '''
        if setting.TELEGRAM['SEND_MSG']:
            sp.call(["notify-send", "-i", str(pathlib.Path.cwd()) + '/deepnlpf/modules/notifications/img/' + icon + '.png', title, mensage])