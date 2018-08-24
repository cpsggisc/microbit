from microbit import *

while True:
	x = accelerometer.get_x()
	y = accelerometer.get_y()
	
	if x > 200:
		display.show("R")
	elif x < -200 :
		display.show("L")
	elif y > 200:
		display.show("D")
	elif y < -200 :
		display.show("U")
	else: # stationary
		display.show("-")
