from .sx127x import SX127x

class LoRa:
    def __init__(self,
                SCK=14,
                MOSI=13,
                MISO=12,
                NSS=15,
                RESET=4,
                DIO0=5,
                name="LoRa",
                ONBOARD_LED=2,
                board="ESP8266",
                callback=None,
                *args,
                **kwargs):
        
        from .esp_controller import Controller
        self.board = board
        
        # initialize lora controller based on board
        self.controller = Controller(
            pin_id_reset=self.get_pin_id(RESET),
            pin_id_led=self.get_pin_id(ONBOARD_LED)
        )
        
        # set pin ids for lora module connection
        self.controller.PIN_ID_SCK = self.get_pin_id(SCK)
        self.controller.PIN_ID_MOSI = self.get_pin_id(MOSI)
        self.controller.PIN_ID_MISO = self.get_pin_id(MISO)
        self.controller.PIN_ID_FOR_LORA_SS = self.get_pin_id(NSS)
        self.controller.PIN_ID_FOR_LORA_DIO0 = self.get_pin_id(DIO0)
        
        # initialize lora radion communication client
        self.client = self.controller.add_transceiver(
            SX127x(name=name, *args, **kwargs),
            pin_id_ss=self.controller.PIN_ID_FOR_LORA_SS,
            pin_id_RxDone=self.controller.PIN_ID_FOR_LORA_DIO0
        )
        
        # set message received callback
        self.client.onReceive(callback or self.on_receive)
    
    def get_pin_id(self, pin):
        if hasattr(pin, 'id'):
            return pin.id
        if isinstance(pin, int):
            return pin
        if isinstance(pin, str):
            from common.pin import mapping
            return mapping[self.board][pin]
    
    def on_receive(self, context, payload):
        context.blink_led()
        try:
            message = payload.decode()
            rssi = context.packetRssi()
            print("message: {}, rssi: {}".format(message, rssi))
        except Exception as e:
            print(e)
    
    def send(self, message):
        self.client.println(message)
    
    def receive(self):
        self.client.receive()