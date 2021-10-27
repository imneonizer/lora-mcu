#! /bin/bash
# script to work with esp8266 based nodemcu

DEVICE="/dev/ttyUSB$1"

# validate device
if [ ! "$DEVICE" ]; then
    echo "No port provided, choose one:"
    echo "`ls /dev/ttyUSB*`"
else
    if [ ! "`ls $DEVICE`" ];then
        echo "Device not found: $DEVICE"
    else
        echo "Using: $DEVICE"
        export AMPY_PORT=$DEVICE
        export AMPY_BAUD=115200
        alias mcu="picocom -b $AMPY_BAUD $AMPY_PORT"
        alias mcp="ampy put"
        alias mpy="ampy run"
        alias deploy="ampy put lib; ampy put src; ampy put main.py"
        alias rcp='_(){ ampy put $1 $1; }; _'
    fi
fi