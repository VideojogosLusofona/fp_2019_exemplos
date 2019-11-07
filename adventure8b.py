room_desc = [
    [ "Room description 0, 0", "Room description 1, 0", "Room description 2, 0", "Room description 3, 0", "Room description 4, 0" ],
    [ "Room description 0, 1", "Room description 1, 1", "Room description 2, 1", "Room description 3, 1", "Room description 4, 1" ],
    [ "Room description 0, 2", "Room description 1, 2", "You are on a path in front of a big building to the south.\nThere is a tree with a squirrel playing in its branches.", "Room description 3, 2", "Room description 4, 2" ],
    [ "Room description 0, 3", "Room description 1, 3", "You seem to have stepped into a library.\n[[BookcaseDescription]][[BookDescription]]", "Room description 3, 3", "Room description 4, 3" ],
    [ "Room description 0, 4", "Room description 1, 4", "Room description 2, 4", "Room description 3, 4", "Room description 4, 4" ],
]

# "You seem to have stepped into a library.\nThere is a large bookcase in the south wall."

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
        [ False, False, True, True ],
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

exit_name = [ "north", "east", "south", "west" ]
exit_inc = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]

game_state = {
    "HasPulledBook" : False,
    "HasExaminedBookcase" : False,
    "BookcaseDescription" : "There is a large bookcase in the south wall.",
    "BookDescription" : ""
}

def show_room_description(x,y):
    s = room_desc[y][x]

    while ("[[" in s):
        i1 = s.index("[[")
        i2 = s.index("]]")
        keyword = s[i1+2:i2]

        if (keyword in game_state):
            s = s[0:i1] + game_state[keyword] + s[i2 + 2:]    
        else:
            s = s[0:i1] + s[i2 +2:]

    print(s)

    nExits = room_exits[y][x].count(True)

    if (nExits == 0):
        print("There are no visible exits.")
    elif (nExits == 1):
        direction = room_exits[y][x].index(True)
        e = exit_name[direction]
        print("There is an exit to the " + e + ".")
    else:
        s = "There are exits to the "
        available_exits = room_exits[y][x]
        count = 0
        for i in range(0, len(available_exits)):
            if (available_exits[i]):
                s = s + exit_name[i]
                if (count < (nExits - 2)):
                    s = s + ", "
                elif (count < (nExits - 1)):
                    s = s + " and "
                else:
                    s = s + "."
                count = count + 1

        print(s)

def move_player(direction_text, direction_index, x_inc, y_inc):
    global x,y
    global room_desc
    global room_exits
    if (room_exits[y][x][direction_index]):
        print("You move " + direction_text + "...")
        x = x + x_inc
        y = y + y_inc
        show_room_description(x,y)
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
    
    if (len(params) == 1):
        print("Use what?")
        return
    if (len(params) < 3):
        print("Where do you want to use " + params[1])
        return

    tmp = ( params[1], params[2] )

    if (tmp in object_usage):
        object_usage[tmp]()
    else:
        print("I'm not sure what you want me to do with " + params[1])

def examine_bookcase_2_3():
    print("There is a book without dust.")
    game_state["HasExaminedBookcase"] = True
    game_state["BookDescription"] = "\nThere is a dustless book on a shelf."

inspectable_objects = {
    ("bookcase", 2, 3) : examine_bookcase_2_3
}

def look_at_something(params):
    if (len(params) == 1):
        show_room_description(x, y)
        return

    tmp = (params[1], x, y)

    if (tmp in inspectable_objects):
        inspectable_objects[tmp]()
    else:
        if (params[1] in room_desc[y][x]):
            print("You don't see anything remarkable about " + params[1])
        else:
            print("I don't see a " + params[1])

def open_passage(x, y, direction):
    room_exits[y][x][direction] = True

    nx = x + exit_inc[direction][0]
    ny = y + exit_inc[direction][1]
    ndirection = (direction + 2) % 4

    room_exits[ny][nx][ndirection] = True

def pull_book_at_2_3():
    global game_state

    if (not game_state["HasExaminedBookcase"]):
        print("I can't see any book...")
        return

    if (game_state["HasPulledBook"]):
        print("You pull the book, nothing happens...")
        return

    print("You hear a click, and the bookcase slides to the side, revealing a secret passage.")

    open_passage(x,y,2)

    game_state["BookcaseDescription"] = "The bookcase has slided to the side, revealing a dark passage."

    show_room_description(x, y)    

pullable_objects = {
    ("book", 2, 3) : pull_book_at_2_3
}

def pull_something(params):
    if (len(params) == 1):
        print("Pull what?")
        return

    tmp = (params[1], x, y)

    if (tmp in pullable_objects):
        pullable_objects[tmp]()
    else:
        if (params[1] in room_desc[y][x]):
            print("You try to pull " + params[1] + ", but fail miserably at it.")
        else:
            print("I don't see a " + params[1])

command_processor = {
    "north" : move_north,
    "n" : move_north,
    "east": move_east,
    "e": move_east,
    "south": move_south,
    "s": move_south,
    "west": move_west,
    "w": move_west,
    "use": use_object,
    "look": look_at_something,
    "examine": look_at_something,
    "pull": pull_something
}

print("----------------------------------------")
x, y = 2, 2
show_room_description(x,y)

input_string = ""
while (input_string != "exit"):    
    print("")
    print("What now?")
    input_string = input()
    input_string = input_string.strip()
    input_string = input_string.lower()
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
        