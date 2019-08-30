room_desc = [
    [ "Room description 0, 0", "Room description 1, 0", "Room description 2, 0", "Room description 3, 0", "Room description 4, 0" ],
    [ "Room description 0, 1", "Room description 1, 1", "Room description 2, 1", "Room description 3, 1", "Room description 4, 1" ],
    [ "Room description 0, 2", "Room description 1, 2", "Room description 2, 2", "Room description 3, 2", "Room description 4, 2" ],
    [ "Room description 0, 3", "Room description 1, 3", "Room description 2, 3", "Room description 3, 3", "Room description 4, 3" ],
    [ "Room description 0, 4", "Room description 1, 4", "Room description 2, 4", "Room description 3, 4", "Room description 4, 4" ],
]

room_exits = [
    [ 
        [ False, False, True, False ],
        [ False, True, False, False ],
        [ False, True, True, True ],
        [ False, True, True, True ],
        [ False, False, True, True ]
    ],
    [ 
        [ True, False, True, False ],
        [ False, True, True, False ],
        [ True, True, True, True ],
        [ True, False, False, True ],
        [ True, False, True, False ]
    ],
    [ 
        [ True, False, True, False ],
        [ True, False, False, False ],
        [ True, False, True, False ],
        [ False, True, False, False ],
        [ True, False, True, True ]
    ],
    [ 
        [ True, False, True, False ],
        [ False, True, True, False ],
        [ True, True, False, True ],
        [ False, True, False, True ],
        [ True, False, True, False ]
    ],
    [ 
        [ True, True, False, False ],
        [ True, False, False, True ],
        [ False, False, False, False ],
        [ True, False, False, False ],
        [ True, False, False, False ]
    ]
]

print("----------------------------------------")
x, y = 2, 2

command = ""
while (command != "exit"):
    print(room_desc[y][x])
    print("")
    print("What now?")
    command = input()

    if (command == "north"):
        # Check if we can move north
        if (room_exits[y][x][0]):
            # Move north
            print("You move north...")
            y = y - 1
        else:
            print("Can't move north!")
    elif (command == "south"):
        # Check if we can move south
        if (room_exits[y][x][2]):
            # Move south
            print("You move south...")
            y = y + 1
        else:
            print("Can't move south!")
    elif (command == "east"):
        # Check if we can move east
        if (room_exits[y][x][1]):
            # Move east
            print("You move east...")
            x = x + 1
        else:
            print("Can't move east!")
    elif (command == "west"):
        # Check if we can move west
        if (room_exits[y][x][3]):
            # Move west
            print("You move west...")
            x = x - 1
        else:
            print("Can't move west!")
    elif (command == "up"):
        print("You move up...")
    elif (command == "down"):
        print("You move down...")
    elif (command == "exit"):
        pass
    else:
        print("I don't understand " + command + "!")
    
    print()

        