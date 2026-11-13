#Name:
#Class: 6th Hour
#Assignment: HW16
import random

import attempt
import attempts

#1. import the "random" library

#2. print "Hello World!"
print("hello world")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("enter a number"))
b = int(input("enter another number"))
c = int(input("enter another number"))
#4. Add a and b together, then divide the sum by c. Print the result.
d= (( a + b )/c)
print(d)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
round(d)
if d % 2 == 0:
    print("even")
else:
    print("odd")
#6. Create a list of five different random integers between 1 and 10.
randlist = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
#7. Print the 4th number in the list.
print(randlist[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
randlist.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
randlist.sort()
print(randlist[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += 1
#11. Create a list containing the names of five other students in the classroom.
name = ["nate","owyn","raphael","misa","braylee"]
#12. Create a for loop that individually prints out the names of each student in the list.
for i in name:
    print(i)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for i in range (0,101):
    if i % 10 == 0 and i != 100:
        break
        print(i)
#14. Free space. Do something creative. :)

var = Exception

import random
attempts = 0
lowerb = int(input(" lowest number you want "))
upperb = int(input(" highest number you want "))
guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
number = random.randint(lowerb,upperb)
if upperb <= 50:
 attempts = 0
 max_attempts = 3
else:
 attempts = 0
 max_attempts = 3
for attempt in range(1, attempts + 1):
     # Input validation to prevent crashing
    try:
         attempts += 1
         guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
    except ValueError:
         print("Invalid input! Please enter a whole number.")
         continue

        # Check the guess
    if guess < number:
            print("Too low! ️")
    elif guess > number:
            print("Too high! ")
    else:
            print(f"\n Congratulations! You guessed the number {number} in {attempt} attempts!")
            break

else:
    print(f"\n Game Over! You've run out of tries. The number was {number}.")

# Run the game
def start_game():
    pass


if __name__ == "__main__":
    while True:
        start_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye.")
            break
