#Name:nate
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random
from random import shuffle

#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
randomint1 = random.randint(1,100)
randomint2 = random.randint(1,100)
randomint3 = random.randint(1,100)
#4. Print the three variables from #3 on the same line.
print(randomint1,randomint2,randomint3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
sumrandomint1 = randomint1 + 2
diffrandomint2 = randomint2 -2
multrandomint3 = randomint3 * 2
#6. Print each result from #5 on the same line.
print(sumrandomint1,diffrandomint2,multrandomint3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
randlist=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
randlist.sort()
print(randlist)
#9. Add together the highest three numbers in the list from #7 and print the result.
sumrandlist=randlist[0] + randlist[1] + randlist[2] + randlist[3]
#10. Create a list with 5 names of other students in this class and print the list.
namelist=["brody","jerell","owen","tucker","huxley"]
#11. Shuffle the list in #10 and print the list again.
shuffle(namelist)
print(namelist)
#12. Print a random choice from the list of names from #10.
print(namelist[random.randint(0,len(namelist)-1)])