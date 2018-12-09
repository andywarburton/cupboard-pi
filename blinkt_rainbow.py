#!/usr/bin/env python

import colorsys
import time

import blinkt

spacing = 360.0 / 16.0
hue = 0

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

while True:

	blinkt.set_pixel(1, 255, 0, 0)
        
	blinkt.show()
	time.sleep(1)
