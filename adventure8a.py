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
print(room_desc[y][x])

def move_player(direction_text, direction_index, x_inc, y_inc):
    global x,y
    global room_desc
    global room_exits
    if (room_exits[y][x][direction_index]):
        print("You move " + direction_text + "...")
        x = x + x_inc
        y = y + y_inc
        print(room_desc[y][x])
    else:
        print("You can't move " + direction_text)

    return True

move_north = lambda params : move_player("north", 0, 0, -1)
move_east = lambda params : move_player("east", 1, 1, 0)
move_south = lambda params : move_player("south", 2, 0, 1)
move_west = lambda params : move_player("west", 3, -1, 0)

object_usage = {
    ("shovel", "dirt") : lambda : print("You dig")
}

def use_object(params):
    tmp = ( params[1], params[2] )

    if (tmp in object_usage):
        object_usage[tmp]()
    else:
        print("I'm not sure what you want me to do with " + params[1])

command_processor = {
    "north" : move_north,
    "n" : move_north,
    "east": move_east,
    "e": move_east,
    "south": move_south,
    "s": move_south,
    "west": move_west,
    "w": move_west,
    "use": use_object
}

input_string = ""
while (input_string != "exit"):    
    print("")
    print("What now?")
    input_string = input()
    input_string = input_string.strip()
    if (input_string == ""):
        continue

    phrase = input_string.split()
    command = phrase[0]

    if (command in command_processor):
        command_processor[command](phrase)
    elif (command == "exit"):
        break
    elif (command == "quit"):
        break
    else:
        print("I don't understand " + command + "!")
    
    print()

print("Goodbye...")
        