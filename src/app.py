import config
from lora import LoRa

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
    context.blink_led()
    try:
        message = payload.decode()
        rssi = context.packetRssi()
        print("message: {}, rssi: {}".format(message, rssi))
    except Exception as e:
        print(e)

lora.client.onReceive(on_receive)

while True:
    if config.NODE_NAME == "7d7e7900":
        now = time.ticks_ms()
        if now < lastSendTime:
            lastSendTime = now 

        if (now - lastSendTime > interval):
            lastSendTime = now
            interval = (lastSendTime % config.INTERVAL)
            message = "{} {}".format(config.NODE_NAME, msgCount)
            lora.send(message)
            msgCount += 1
    else:
        lora.client.receive()
        time.sleep_ms(config.INTERVAL)