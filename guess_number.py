from microbit import *
import random

guess = 0
random_number = 0

while True:
  if button_a.get_presses():
    guess = guess + 1
    display.show(str(guess))
  elif button_b.is_pressed():
    break

numbers = [1,2,3,4,5]
random_number = random.choice(numbers)

if guess == random_number:
  display.show(Image.HAPPY)
else:
  display.show(Image.SAD)
  sleep(1000)
  display.show(str(random_number))
