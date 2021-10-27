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
NODE_NAME = get_uuid()
INTERVAL = 50 #ms