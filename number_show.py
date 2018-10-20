#!/usr/bin/env python

from time import sleep
import unicornhat as unicorn
import numpy as np
from mnist_detect import mnist_detect

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

zero = [
     "  XXXX  "
    ," X    X "
    ,"XX    XX"
    ,"XX    XX"
    ,"XX    XX"
    ,"XX    XX"
    ," X    X "
    ,"  XXXX  "
    ]


one = [
     "   XX   "
    ,"  XXX   "
    ,"   XX   "
    ,"   XX   "
    ,"   XX   "
    ,"   XX   "
    ,"   XX   "
    ,"  XXXX  "
    ]

two = [
     "  XXXX  "
    ,"  X  X  "
    ,"  X  X  "
    ,"     X  "
    ,"    XX  "
    ,"   XX   "
    ,"  XX    "
    ,"  XXXX  "
    ]

three = [
     "  XXX   "
    ,"  X  X  "
    ,"     X  "
    ,"  XXX   "
    ,"  XXX   "
    ,"     X  "
    ,"  X  X  "
    ,"  XXX   "
    ]

four = [
     "   XXX  "
    ,"   X X  "
    ,"  X  X  "
    ,"  X  X  "
    ," X   X  "
    ," XXXXXX "
    ,"     X  "
    ,"     X  "
    ]

five = [
     "  XXXX  "
    ,"  X     "
    ,"  X     "
    ,"  XXX   "
    ,"     X  "
    ,"  x  X  "
    ,"  X  X  "
    ,"  XXX   "
    ]

six = [
     "  XXXX  "
    ,"  X  X  "
    ,"  X     "
    ,"  XXXX  "
    ,"  X  X  "
    ,"  X  X  "
    ,"  X  X  "
    ,"  XXXX  "
    ]

seven = [
     "  XXXX  "
    ,"  X  X  "
    ,"  X  X  "
    ,"     X  "
    ,"     X  "
    ,"     X  "
    ,"     X  "
    ,"     X  "
    ]

eight = [
     "  XXXX  "
    ,"  X  X  "
    ,"  X  X  "
    ,"   XX   "
    ,"   XX   "
    ,"  X  X  "
    ,"  X  X  "
    ,"  XXXX  "
    ]

nine = [
     "  XXXX  "
    ,"  X  X  "
    ,"  X  X  "
    ,"  XXXX  "
    ,"     X  "
    ,"     X  "
    ,"  X  x  "
    ,"  XXXX  "
    ]

mnist_num = [zero, one, two, three, four, five, six, seven, eight, nine]

def mnist_show():
    y = mnist_detect()
    for h in range(height):
        for w in range(width):
            chr = mnist_num[y][h][w]
            if chr == ' ':
                unicorn.set_pixel(w, h, 0, 0, 0)
            else:
                unicorn.set_pixel(w, h, 0, 0, 255)
    unicorn.show()

while True:
    mnist_show()
    sleep(0.1)
