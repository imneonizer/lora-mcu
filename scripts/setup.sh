#! /bin/bash
# script to work with esp8266 based nodemcu

DEVICE="/dev/ttyUSB$1"

# check if script is being sourced
if [[ ! "${BASH_SOURCE[0]}" != "${0}" ]];then
    echo "Usage: source $0"
    exit
fi

# install dev tools: esptool, adafruit-ampy
if [ "`pip -V`" ];then
    # check esptool.py
    if [ ! "`pip freeze | grep -i esptool`" ];then
        pip install esptool.py
    fi

    # check ampy
    if [ ! "`pip freeze | grep -i adafruit-ampy`" ];then
        pip install adafruit-ampy
    fi
else
    echo "pip not found"
    exit -1
fi