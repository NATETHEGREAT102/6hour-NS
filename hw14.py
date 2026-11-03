#Name:nate
#Class: 6th Hour
#Assignment: HW14
import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.

i = 5
while i>=0:
    print(i)
    i = i - 1

else:

    print("hello world")

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
j = 1
while j <= 30:
    if j % 2 == 0:
         print(j)
    j += 1

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
y = 1
while y <= 30:
    if y % 3 != 0:
        print(y)
    y += 1

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
while True:
    z = random.randint(1,6)
    print(z)
    if z == 1:
        break


#5. Create a while loop that asks for a number input until the user inputs the number 0.
while True:
    zero = float(input("input a number"))
    if zero == 0:
        print("you broke it")
        break
