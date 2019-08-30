print("What now?")
command = input()

if (command == "north"):
    print("You move north...")
elif (command == "south"):
    print("You move south...")
elif (command == "east"):
    print("You move east...")
elif (command == "west"):
    print("You move west...")
elif (command == "up"):
    print("You move up...")
elif (command == "down"):
    print("You move down...")
else:
    print("I don't understand " + command + "!")
    