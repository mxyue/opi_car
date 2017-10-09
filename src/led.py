#import the library
from pyA20.gpio import gpio
from pyA20.gpio import connector
from time import sleep

gpio.init()

pin1 = connector.gpio1p7

gpio.setcfg(pin1, gpio.INPUT)

valueBefore = gpio.input(pin1)
print('before value->', valueBefore)

while True:
    value = gpio.input(pin1)
    if valueBefore != value :
        valueBefore = value
        print("value->", value)
