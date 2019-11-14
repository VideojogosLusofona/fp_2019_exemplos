class Room:
    description = ""
    exits = [ False, False, False, False, False ]
    x = 0
    y = 0

    def __init__(self, x, y, desc, north, east, south, west):
        self.description = desc
        self.exits = [ north, east, south, west ]
        self.x = x
        self.y = y

    def CanExit(self, dir):
        return self.exits[dir]

    def GetExitCount(self):
        return self.exits.count(True)

    def GetItems(self):
        ret = []

        for item in items:
            if ((item.position == (self.x, self.y)) and (not item.inInventory)):
                ret.append(item)

        return ret

    def ShowRoomDescription(self):
        s = self.description

        while ("[[" in s):
            i1 = s.index("[[")
            i2 = s.index("]]")
            keyword = s[i1+2:i2]

            if (keyword in game_state):
                s = s[0:i1] + game_state[keyword] + s[i2 + 2:]    
            else:
                s = s[0:i1] + s[i2 +2:]

        print(s)

        nExits = self.GetExitCount()

        if (nExits == 0):
            print("There are no visible exits.")
        elif (nExits == 1):
            direction = self.exits.index(True)
            e = exit_name[direction]
            print("There is an exit to the " + e + ".")
        else:
            s = "There are exits to the "
            available_exits = self.exits
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

        items_in_room = self.GetItems()

        if (len(items_in_room) == 0):
            pass
        elif (len(items_in_room) == 1):
            print("You can see a " + items_in_room[0].name)
        else:
            s = "You can see "
            count = 0
            nItems = len(items_in_room)
            for i in range(0, len(items_in_room)):
                s = s + items_in_room[i].name
                if (count < (nItems - 2)):
                    s = s + ", "
                elif (count < (nItems - 1)):
                    s = s + " and "
                else:
                    s = s + "."
                count = count + 1

            print(s)

    def OpenPassage(self, direction):
        global rooms

        self.exits[direction] = True

        nx = self.x + exit_inc[direction][0]
        ny = self.y + exit_inc[direction][1]
        ndirection = (direction + 2) % 4

        rooms[ny][nx].exits[ndirection] = True

class Item:
    name = ""
    description = ""
    position = (0,0)
    inInventory = False

    def __init__(self, name, position, description):
        self.name = name
        self.description = description
        self.position = position
        self.inInventory = False

rooms = [
    [ 
        Room(0, 0, "Room description 0, 0", False, False, True, False ),
        Room(1, 0, "Room description 1, 0", False, True, False, False ),
        Room(2, 0, "Room description 2, 0", False, True, True, True ),
        Room(3, 0, "Room description 3, 0", False, True, True, True ),
        Room(4, 0, "Room description 4, 0", False, False, True, True )
    ],
    [ 
        Room(0, 1, "Room description 0, 1", True, False, True, False ),
        Room(1, 1, "Room description 1, 1", False, True, True, False ),
        Room(2, 1, "Room description 2, 1", True, True, True, True ),
        Room(3, 1, "Room description 3, 1", True, False, False, True ),
        Room(4, 1, "Room description 4, 1", True, False, True, False )
    ],
    [ 
        Room(0, 2, "Room description 0, 2", True, False, True, False ),
        Room(1, 2, "Room description 1, 2", True, False, False, False ),
        Room(2, 2, "You are on a path in front of a big building to the south.\nThere is a tree with a squirrel playing in its branches.", True, False, True, False ),
        Room(3, 2, "Room description 3, 2", False, True, False, False ),
        Room(4, 2, "Room description 4, 2", True, False, True, True )
    ],
    [ 
        Room(0, 3, "Room description 0, 3",  True, False, True, False ),
        Room(1, 3, "Room description 1, 3",  False, True, True, False ),
        Room(2, 3, "You seem to have stepped into a library.\n[[BookcaseDescription]][[BookDescription]]",  True, True, False, True ),
        Room(3, 3, "Room description 3, 3",  False, True, False, True ),
        Room(4, 3, "Room description 4, 3",  True, False, True, False )
    ],
    [ 
        Room(0, 4, "Room description 0, 4",  True, True, False, False ),
        Room(1, 4, "Room description 1, 4",  True, False, False, True ),
        Room(2, 4, "Room description 2, 4",  False, False, False, False ),
        Room(3, 4, "Room description 3, 4",  True, False, False, False ),
        Room(4, 4, "Room description 4, 4",  True, False, False, False )
    ]
]

items = [
    Item("apple", (2,2), "A shiny red apple"),
    Item("bottle", (2,2), "A bottle full of water")
]

exit_name = [ "north", "east", "south", "west" ]
exit_inc = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]
x, y = 2, 2

game_state = {
    "HasPulledBook" : False,
    "HasExaminedBookcase" : False,
    "BookcaseDescription" : "There is a large bookcase in the south wall.",
    "BookDescription" : ""
}

def move_player(direction_text, direction_index, x_inc, y_inc):
    global x,y
    global rooms

    current_room = rooms[y][x]

    if (current_room.CanExit(direction_index)):
        print("You move " + direction_text + "...")
        x = x + x_inc
        y = y + y_inc
        current_room = rooms[y][x]
        current_room.ShowRoomDescription()
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
        current_room = rooms[y][x]
        current_room.ShowRoomDescription()
        return

    tmp = (params[1], x, y)

    if (tmp in inspectable_objects):
        inspectable_objects[tmp]()
    else:
        if (params[1] in rooms[y][x].description):
            print("You don't see anything remarkable about " + params[1])
        else:
            print("I don't see a " + params[1])

def pull_book_at_2_3():
    global game_state

    if (not game_state["HasExaminedBookcase"]):
        print("I can't see any book...")
        return

    if (game_state["HasPulledBook"]):
        print("You pull the book, nothing happens...")
        return

    print("You hear a click, and the bookcase slides to the side, revealing a secret passage.")

    current_room = rooms[y][x]
    current_room.OpenPassage(2)

    game_state["BookcaseDescription"] = "The bookcase has slided to the side, revealing a dark passage."

    current_room.ShowRoomDescription()

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
        if (params[1] in rooms[y][x].description):
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
current_room = rooms[y][x]
current_room.ShowRoomDescription()

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
        