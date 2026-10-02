#Name:nate
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
enemy = {
    "bob" : {
        "damage":2324,
         "health" : 45,
        "power" : 50,
        "shield" : 1203
    },

        " not bob" : {
        "damage":93,
        "health": 45344534556354,
        "power": 22,
        "shield":23545
    },
    "jimothy" : {
        "damage":434,
        "health" : 32432,
        "power" : 34,
        "shield" :1233545,
    },
    "charry" : {
        "damage":434,
        "health" : 345,
        "power" : 124,
        "shield" :44545,
    },
    "john" : {
        "damage":434,
        "health" : 52,
        "power" : 64,
        "shield" :878,

    },
}
enemy_list =input("select enemy, bob, not bob, jimothy, charry, john ")
print(enemy[enemy_list])

enemy_changes =input("select enemy stat to change: damage health power shield")
new_stat = int(input("input new stat: "))
enemy[enemy_list].update({enemy_changes:new_stat})
print(enemy[enemy_list])