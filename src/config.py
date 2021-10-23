import os 
from common import get_uuid

# LoRa Pin config
NSS = 'D8'
MOSI = 'D7'
MISO = 'D6'
SCK = 'D5'
RESET = 'D2'
DIO0 = 'D1'

# payload config
NODE_NAME = "{}_{}".format(os.uname().sysname, get_uuid())
INTERVAL = 500 #ms