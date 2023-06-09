my_number = "5"

# this is an iteration/loop
while True:

    user_guess = input("Please guess my number which is between 1 and 10: ")  #"From user received data is always in string type"

    if user_guess == my_number:
        print("You guessed it. Bravooo!")

        wants_repeat = input("Do you want to play again? (y/n)")

        if wants_repeat == 'y':
            continue
        else:
            break
        
    else:
        print('Bad guess! Try again !')



print("Good bye! We expect you again !")

    