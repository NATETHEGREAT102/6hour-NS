#Name:nate
#Class: 6th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
numlist=[1,2,3,4,5,6,7,8,9]
print(numlist)
#2. Sort the list from highest to lowest.
numlist.sort(reverse=True)
#3. Create an empty list.
emplist=[]
#4. Remove the median number from the first list and add it to the second list.
numlist.pop(4)
#5. Remove the first number from the first list and add it to the second list.
numlist_sum = numlist + emplist
#6. Print both lists.
print(numlist_sum)
#7. Add the two numbers in the second list together and print the result.
numlist_sum=numlist[1]+numlist[2]
print(numlist_sum)
#8. Add the sum from #7 to the first list.
numlistallsum=numlist+numlist_sum
print(numlistallsum)
#9. Sort the first list from lowest to highest and print it.
numlist.sort(reversed=False)