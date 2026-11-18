#Name:nate
#Class: 6th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings

ratinglist=[]
players =int(input("number of players "))
for i in range(players):
    rating=int(input(f"player {i+1} rating (1-5): "))
    if rating > 5 or rating < 1:
        valid=False
        print("invalid rating")
        break
    valid=True
    ratinglist.append(rating)
if valid:
    ratingAV=sum(ratinglist)/players
    print(round(ratingAV,2))





