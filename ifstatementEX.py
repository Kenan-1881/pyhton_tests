weight = int(input("Give weight: "))
unit = input("(k)g or (l)bs: ")
if unit == "k":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("weight in Kgs: " + str(converted))

height = int(input("Give height: "))
unit = input("(m) or (cm): ")
if unit == "m":
    converted = height * 100
    print ("height in cm: " + str(converted))
else:
    converted = height / 100
    print("height in m: " + str(converted))
