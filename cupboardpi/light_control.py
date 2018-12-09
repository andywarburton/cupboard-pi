#!/usr/bin/env python

import time
import signal
import touchphat
from mote import Mote

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

# flash the lights on bootup
for pad in ['Back','A','B','C','D','Enter']:
    touchphat.set_led(pad, True)
    time.sleep(0.1)
    touchphat.set_led(pad, False)
    time.sleep(0.1)

@touchphat.on_touch(['Back','A','B','C','D','Enter'])
def handle_touch(event):

	print(event.name)

	if(event.name == 'A'):
		# bright white
		r = 255
		g = 255
		b = 255
	elif(event.name == 'B'):
		# less white
		r = 50
		g = 50
		b = 50
	elif(event.name == 'C'):
		# yellowwy
		r = 150
		g = 50
		b = 0
	elif(event.name == 'D'):
		# red
		r = 150
		g = 0
		b = 0
	elif(event.name == 'Back' or event.name == 'Enter'):
		# LIGHTS OUT
		r = 0
		g = 0
		b = 0

	for channel in range(4):
		for pixel in range(16):
			mote.set_pixel(channel + 1, pixel, r, g, b)
	
	mote.show()

signal.pause()

