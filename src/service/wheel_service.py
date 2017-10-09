# -*- coding:utf-8 -*-

#import the library
from pyA20.gpio import gpio
from pyA20.gpio import connector
from time import sleep

gpio.init()

# r1
pinR11 = connector.gpio1p31
pinR12 = connector.gpio1p33

# r2
pinR21 = connector.gpio1p38
pinR22 = connector.gpio1p40

# l1
pinL11 = connector.gpio1p35
pinL12 = connector.gpio1p37

#l2
pinL21 = connector.gpio1p32
pinL22 = connector.gpio1p36


def setHighPin(pin):
        gpio.setcfg(pin, gpio.OUTPUT)
        gpio.output(pin, gpio.HIGH)


def setLowPin(pin):
        gpio.setcfg(pin, gpio.INPUT)


def stop():
        for pin in [pinR11, pinR12, pinR21, pinR22, pinL11, pinL12, pinL21, pinL22]:
                setLowPin(pin)


def switch(p1, p2, f):
        if f == 1:
                setHighPin(p1)
                setLowPin(p2)
        elif f == -1:
                setHighPin(p2)
                setLowPin(p1)
        elif f == 0:
                setLowPin(p1)        
                setLowPin(p2)


def r1(f):
        switch(pinR11, pinR12, f)      

def r2(f):
        switch(pinR21, pinR22, f)

def l1(f):
        switch(pinL11, pinL12, f)

def l2(f):
        switch(pinL21, pinL22, f)


def control(angle, distance):
        if distance == 0 :
                stop()
        if angle > 22 and angle <= 67:
                #右上
                r1(0)
                r2(0)
                l1(1)
                l2(1)
        elif angle > 67 and angle <= 112:
                #上
                r1(1)
                r2(1)
                l1(1)
                l2(1)
        elif angle > 112 and angle <= 157:
                #左上
                r1(1)
                r2(1)
                l1(0)
                l2(0)
        elif angle > 157 and angle <= 202:
                #左
                r1(1)
                r2(1)
                l1(-1)
                l2(-1)
        elif angle > 202 and angle <= 247:
                #左下
                r1(-1)
                r2(-1)
                l1(0)
                l2(0)
        elif angle > 247 and angle <= 292:
                #下
                r1(-1)
                r2(-1)
                l1(-1)
                l2(-1)
        elif angle > 292 and angle <= 337:
                #左下
                r1(0)
                r2(0)
                l1(-1)
                l2(-1)
        else:
                #右
                r1(-1)
                r2(-1)
                l1(1)
                l2(1)



