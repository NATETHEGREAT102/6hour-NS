#Name:nate
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World")

#2. Create a list with three variables that each randomly generate a number between 1 and 100
randlist =[random.randint(0,100),random.randint(0,100),random.randint(0,100)]
#3. Print the list.
print(randlist)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if randlist[0]>randlist[1] and randlist[0] > randlist[2]:
    print()
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.