#Name:nate
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
dictionar= {
    "key1":"value1",
    "key2":"value2",
    "key3":[1,43,34,45],
}
print(dictionar)
#3. Print the keys of the dictionary from #2.
print(dictionar.keys())
#4. Print the values of the dictionary from #2
print(dictionar.values())
#5. Print one of the three numbers from the list by itself
print(dictionar["key3"][3])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
dictionar.update({"key4":"value4"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(dictionar)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
class_mates = {
    "peer1" : {
        "Name" : "Owyn",
        "Grade" : 9,
        "AGE" : 14,
    },
    "peer2" : {
        "Name" : "Jerrell",
        "Grade" : 9,
        "AGE" : 15,
    },
     "peer3" : {
        "Name" : "Brody",
        "Grade" : 9,
        "AGE" : 14,
    },
}
print(class_mates)


#9. Print the names of all three classmates on the same line.
print(class_mates["peer1"]["Name"],class_mates["peer2"]["Name"],class_mates["peer3"]["Name"])


#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
class_mates.pop("peer2")
print(class_mates)