
user_answer = input('do you want advice on the weather ? (y/n): ')

# Kenan's Comment:  exit() function stops the program and exits
# If you remember:  '!=' ==> means "NOT equal".
# If the user_answer is NOT equal to 'y", then it exits. Otherwise it continues as normal.
# In this way, you save from writing the 'else' statement.

if user_answer != 'y':
    print("Byeeee, have a nice day!")
    exit()

# Kenan's Comment: This is a 'list' of possible answers. The '\n' creates a new line ;-)
replies = [
    "it's  a hot day \n drink water if you go outside!",
    "it's a nice day \n go for a walk!",
    "it's a bit cold day \n get a jacket for outside!",
    "it's freezing! \n don't go outside!"
]

while True:

    temperature = int(input("what is the temperature: "))

    # Kenan's Comment: choose 'what to answer' from the above 'list', in this way your code will be cleaner ;-)
    if temperature > 30:
        print(replies[0])

    elif temperature >= 20:
        print(replies[1])

    elif temperature >= 10:
        print(replies[2])

    else:
        print(replies[3])

    wants_repeat = input("Do you want another advice? (y/n)")

    if wants_repeat == 'y':
        continue
    else:
        break

print('bye!')





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
