#!/usr/bin/env python

import datetime
import time

from microdotphat import write_string, set_decimal, clear, show

while True:
	clear()
	t = datetime.datetime.now()
	write_string(t.strftime('%H:%M'), kerning=False)
	show()
	time.sleep(10)
