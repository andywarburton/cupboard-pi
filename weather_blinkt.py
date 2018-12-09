import openweathermapy as owm
import time
import blinkt


blinkt.set_clear_on_exit()
blinkt.set_brightness(0.05)
settings = { "APPID": 'cf989ed49dcc85f0d4a44cb03939d3b0', "units": "metric" }

colors = {}
colors['white'] = {'r':255,'g':255,'b':255}
colors['blue'] = {'r':0,'g':0,'b':255}
colors['green'] = {'r':0,'g':255,'b':0}
colors['yellow'] = {'r':255,'g':230,'b':0}
colors['orange'] = {'r':255,'g':188,'b':0}
colors['red'] = {'r':255,'g':0,'b':0}


while True:

	data = owm.get_current("Amsterdam,NL", **settings)
	temp = data("main.temp")

	print temp

	if(temp < 5):
		color = 'white'
	elif(temp > 5 and temp <= 10):
		color = 'blue'
	elif(temp > 10 and temp <= 14):
		color = 'green'
	elif(temp > 14 and temp <= 18):
		color = 'yellow'
	elif(temp > 18 and temp <= 21):		
		color = 'orange'
	elif(temp > 21):
		color = 'red'

	blinkt.set_all(colors[color]['r'], colors[color]['g'], colors[color]['b'])
	blinkt.show()

	time.sleep(610)
