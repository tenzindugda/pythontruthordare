# this will.... create a truth or dare?

# if they pick a truth then the computer gives a statment that might put the human in akward position to answer

# if they pick a dare they are told to do some harmless prank at school or on the weekend.

# we need advanced data lists/arreays have a function that sets up those lists at the start of the game.
# like getting monopoly game setup before you can play monopoly. 

# setup empty lists
truthQuestions = []
dareChallenges = []

# define function we need to use later
def setupTruthList(list1):
    # add first item to index zero of the list
    list1.append("Have you ever stolen from your parents")
    list1.append("Who is your crush at FHS")
    list1.append("What teacher do you trust the most")
    list1.append("Have you ever had a crush on a teacher? If so who?
    # this is a local list we pass back to who called us
    return list1

def setupDareList(list1):
    # add first item to index zero of the list
    list1.append("leave a happy note for a teacher")
    list1.append("ask a new student to eat lunch with you")
    list1.append("tell your fav teacher that they are your fav in front of class")
    # this is a local list we pass back to who called us
    return list1



setupTruthList(truthQuestions)
setupDareList(dareChallenges)
# call the function to start the game, then ask a question of the human


user = input("truth? or dare?: ")
#User selects either truth dare by typing in truth  or dare
    

if user == "truth":
	print("here comes your question....")
	print(truthQuestions[0])
#If user types truth, then the code spites out the question
    
    
elif user == "dare":
	print("here comes your dare....")
	print(dareChallenges[0])

#If user types dare, then the code spites out a dare
 
else:
    print("you didn't type it correctly, please type truth or dare")
#If the user doesn't type truth or dare, the code says to retype it 

print("")
print("")
print("")
print("")
print("")
print("")





