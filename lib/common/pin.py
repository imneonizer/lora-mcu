from machine import Pin

def init_pin(name, *args, **kwargs):
    # initialize the pin based on pin number or
    # pin name as printed on node mcu board
    if isinstance(name, int):
        return Pin(name, *args, **kwargs)
    else:
        mapping = {
            "D0": 16,
            "D1": 5,
            "D2": 4,
            "D3": 0,
            "D4": 2,
            "D5": 14,
            "D6": 12,
            "D7": 13,
            "D8": 15,
        }
        return Pin(mapping[name.upper()], *args, **kwargs)