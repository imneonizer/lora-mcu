import config
from lora import LoRa
from common.blink import blink

lora = LoRa(
    NSS='D8',
    MOSI='D7',
    MISO='D6',
    SCK='D5',
    RESET='D2',
    DIO0='D1'
)

import time 
msgCount = 0
millisecond = time.ticks_ms
lastSendTime = 0
interval = 0
st = time.ticks_ms()

def on_receive(context, payload):
    blink(1, 0.03)
    try:
        message = payload.decode()
        rssi = context.packetRssi()
        print("message: {}, rssi: {}".format(message, rssi))
    except Exception as e:
        print(e)

lora.client.onReceive(on_receive)

print("This Node: {}".format(config.NODE_NAME))
while True:
    if config.NODE_NAME == "7d7e7900":
        message = "{} {}".format(config.NODE_NAME, msgCount)
        lora.send(message)            
        blink(1, 0.03)
        print(message)
        msgCount += 1
    else:
        lora.client.receive()
    
    time.sleep_ms(config.INTERVAL)