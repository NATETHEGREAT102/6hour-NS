#Name: nate
#Class: 6th Hour
#Assignment: SC3
import time
#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
fb = 1
while fb <=100:
    time.sleep(0.045)
    if fb % 3 == 0 and fb % 5 == 0:
        print("fizzbuzz")
    elif fb % 3 == 0:
        print("fizz")
    elif fb % 5 == 0:
        print("buzz")
    else:
      print(fb)
    fb +=1