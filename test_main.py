# -*- coding:utf-8 -*-

#import the library
from pyA20.gpio import gpio
from pyA20.gpio import connector
from time import sleep

gpio.init()

pin1 = connector.gpio1p11
pin2 = connector.gpio1p13

def setHighPin(pin):
        gpio.setcfg(pin, gpio.OUTPUT)
        gpio.output(pin, gpio.HIGH)

def setLowPin(pin):
        gpio.setcfg(pin, gpio.INPUT)

setHighPin(pin1)
setLowPin(pin2)
sleep(5)
setHighPin(pin2)
setLowPin(pin1)
sleep(5)
