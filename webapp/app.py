from flask import Flask,request
import datetime
import random

app = Flask(__name__)
#app.run(debug=True)

@app.route('/')

def index():

	# get the user string
	user = request.args.get("user")
	
	# get the day of the week
	day = datetime.datetime.today().weekday()

	# get the time
	a = datetime.datetime.now().time()

	# convert time to a float
	mytime = a.hour+a.minute/60.0

	# default to off
	color = "0,0,0,0"

	# at night time it should be red but not bright red
	if mytime > 0:

		r = 255
		g = 0
		b = 0
		a = 20

	# if the day of the week is Saturday or Sunday we're going to start the program later
	if day >= 5:

		if mytime > 7:
			# orange
			r = 255
			g = 89
			b = 0 
			a = 30


		if mytime > 8:
			# yellow
			r = 255
			g = 255
			b = 0
			a = 50

		if mytime > 8.5:
			# white
			r = 255
			g = 255
			b = 255
			a =	200				

	else:

		# monday to friday

		if user == "harry":

			if mytime > 7:
				# orange
				r = 255
				g = 89
				b = 0 
				a = 30


			if mytime > 7.5:
				# yellow
				r = 255
				g = 255
				b = 0
				a = 50

		if(user == "jack"):

			if(mytime > 5):
				# orange
				r = 255
				g = 33
				b = 0
				a = 150

			if(mytime > 6):
				# brighter orange
				r = 255
				g = 100
				b = 0
				a = 200	

			if(mytime > 6.5):
				# more orangy
				r = 255
				g = 157
				b = 0
				a = 255

			if(mytime > 6.75):
				# yellow
				r = 255
				g = 255
				b = 0			
				a = 255

			if(mytime > 7):
				# white
				r = 255
				g = 255
				b = 255
				a = 255				

		if user == "harry" and mytime > 9:
			# pink
			r = 255
			g = 56
			b = 245
			a = 200

		if user == "jack" and mytime > 9:	
			# blue
			r = 0
			g = 97
			b = 255
			a = 200

	if mytime > 18:
		# yellow
		r = 255
		g = 255
		b = 0			
		a = 255

	if mytime > 18.25:
		# more orangy
		r = 255
		g = 157
		b = 0
		a = 255

	if mytime > 18.5:
		# orange
		r = 255
		g = 33
		b = 0
		a = 150

	if mytime > 18.75:
		# more orangy
		r = 255
		g = 157
		b = 0
		a = 255

	if mytime >= 19:
		# brighter red
		r = 255
		g = 0
		b = 0
		a = 150
	if mytime >= 19.15:
		# dim red
		r = 255
		g = 0
		b = 0
		a = 20


	color = str(r) + "," + str(g) + "," + str(b) + "," + str(a)

	return color

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=666)
