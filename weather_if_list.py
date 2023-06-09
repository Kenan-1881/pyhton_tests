advice = ["it's a hot day", "drink water if you go outside!", 
          "it's a nice day", "go for a walk without worrying about the weather!",
          "it's a bit colder day", "get a jacket for outside!",
          "it's freezing!", "don't go outside!"]
play = 'y'
user_answer = input('do you want advice on the weather ? (y/n)')

while True:
    if user_answer == play:

        temperature = int(input("what is the temperature: "))

        if temperature > 30:
            print("it's a hot day")
            print("drink water if you go outside!")

        elif temperature >= 20:
            print("it's a nice day")
            print("go for a walk without worrying about the weather!")

        elif temperature >= 10:
            print("it's a bit colder day")
            print("get a jacket for outside!")
        
        else:
            print("it's freezing!")
            print("don't go outside!")
        
        wants_repeat = input("Do you want another advice? (y/n)")

        if wants_repeat == 'y':
            continue
        else:
            break
    
    else:
        break
    
print('bye!')


