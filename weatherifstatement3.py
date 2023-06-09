#************************************************************************
# WEATHER ADVICE PROGRAM
# Author: Kiril Tomov
# Gets temperature input from the user and gives the related advice.
# TO DO (Kenan): The user input must be checked if it is a "numeric" data.
#************************************************************************



#------------------------------------------------------------------------
# DATA Definitions
#------------------------------------------------------------------------

# This is a LIST type of collection. Put attention on square brackets []
questions = [
    'Do you want advice on the weather ? (y/n): ',
    'What is the temperature?: ',
    'Do you want another advice? (y/n): '
]

# This is a DICTIONARY type of collection. Put attention on curly brackets {}
advices = {
    "hot"       :"it's  a hot day \n drink water if you go outside! \n",
    "nice"      :"it's a nice day \n go for a walk! \n",
    "cold"      :"it's a bit cold day \n get a jacket for outside! \n",
    "freezing"  :"it's freezing! \n don't go outside! \n"
}

#------------------------------------------------------------------------
# FUNCTION Definitions
#------------------------------------------------------------------------

# This is a function for choosing the related advice from the advices dictionary
# Please Note TO DO: If the 'temp' parameter is not a numeric data, it fails or falls to ERROR ! It needs to be checked.
def get_advice(temp):
    if temp > 30:
        return advices["hot"]
    elif temp >= 20:
        return advices["nice"]
    elif temp >= 10:
        return advices["cold"]
    else:
        return advices["freezing"]

# This is a 'helper' function, for evaluating the user's (y/n) answers to a Boolean True or False.
# So that we can use it multiple times for all (y/n) questions.
# FYI: I on purpose omitted the 'else', for you to see that a function returns the 'first' return which it hits in the 'flow'.
def wants(user_input):
    if user_input != 'y':
        return False
    return True


#------------------------------------------------------------------------
# START of APPLICATION
#------------------------------------------------------------------------

# Gets input: Asks the user if he/she does want to play (wants an advice on weather or not)
to_play = input(questions[0])

# Checks the received answer: Uses wants() function to evaluate the user_input to a "False or True".
# Please note how we use the negation 'not' operator!
if not wants(to_play):
    print("Byeeee, have a nice day!")
    exit()

while True:

    # Gets input: Asks the temperature and casts it to an integer number
    # TO DO: Normally we need to check if the given input is 'numeric'. If user doesn't give a numeric input it fails (falls to ERROR).
    temperature = int(input(questions[1]))

    # Prints the answer using the function for getting the related answer
    print(get_advice(temperature))

    # Asks if user wants another advice (y/n)
    another = input(questions[2])

    if not wants(another):
        break

print('bye!')

#------------------------------------------------------------------------
# END of APPLICATION
#------------------------------------------------------------------------








# YOUR ORIGINAL CODE:

# play = 'y'
# user_answer = input('do you want advice on the weather ? (y/n)')

# while True:
#     if user_answer == play:

#         temperature = int(input("what is the temperature: "))

#         if temperature > 30:
#             print("it's  a hot day")
#             print("drink water if you go outside!")

#         elif temperature >= 20:
#             print("it's a nice day")
#             print("go for a walk!")

#         elif temperature >= 10:
#             print("it's a bit cold day")
#             print("get a jacket for outside!")

#         else:
#             print("it's freezing!")
#             print("don't go outside!")

#         wants_repeat = input("Do you want another advice? (y/n)")

#         if wants_repeat == 'y':
#             continue
#         else:
#             break

#     else:
#         break

# print('bye!')
