def get_mac():
    import network
    import ubinascii
    return ubinascii.hexlify(network.WLAN().config('mac'),':').decode()

def get_serial():
    import machine
    import ubinascii
    serial = ''
    for i in machine.unique_id():
        serial += str(i)
    return serial

def get_ip():
    import network
    return network.WLAN(network.STA_IF).ifconfig()