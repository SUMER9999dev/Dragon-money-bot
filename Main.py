"""
основной entry point
"""

from SeleniumController import Controller
import random
import time
import requests
import eel
import os
from ConfigReader import Reader
import Beta
import Default


controller = None


def wait_for_crash_open():
    while controller.is_crash_opened() != True:
        pass


@eel.expose
def run_bot():
    global controller

    controller = Controller()

    controller.open_website('https://drgn.gold/games/crash')

    if os.path.isfile('cookies.json'):
        controller.load_cookie()

    controller.driver.refresh()

    wait_for_crash_open()

    controller.save_cookie()

    controller.type_auto_conclusion(controller.cfg.auto_conclusion())

    if controller.cfg.tactic() == 'beta':
        Beta.load(controller)
    elif controller.cfg.tactic() == 'default':
        Default.load(controller)
    else:
        try:
            __import__(controller.cfg.tactic(), fromlist=['object']).load(controller)
        except:
            print('Error while loading tactic...')


eel.init('ui')
eel.start('Main.html', size=(300, 200), position=(0,0), port=9090)
