class Room:
    description = ""
    exits = [ False, False, False, False, False ]

    def __init__(self, desc, north, south, east, west):
        self.description = desc
        self.exits = [ north, east, south, west ]

    def CanExit(self, dir):
        return self.exits[dir]

rooms = [
    [ 
        Room("Room description 0, 0", False, False, True, False ),
        Room("Room description 1, 0", False, True, False, False ),
        Room("Room description 2, 0", False, True, True, True ),
        Room("Room description 3, 0", False, True, True, True ),
        Room("Room description 4, 0", False, False, True, True )
    ],
    [ 
        Room("Room description 0, 1", True, False, True, False ),
        Room("Room description 1, 1", False, True, True, False ),
        Room("Room description 2, 1", True, True, True, True ),
        Room("Room description 3, 1", True, False, False, True ),
        Room("Room description 4, 1", True, False, True, False )
    ],
    [ 
        Room("Room description 0, 2", True, False, True, False ),
        Room("Room description 1, 2", True, False, False, False ),
        Room("Room description 2, 2", True, False, True, False ),
        Room("Room description 3, 2", False, True, False, False ),
        Room("Room description 4, 2", True, False, True, True )
    ],
    [ 
        Room("Room description 0, 3",  True, False, True, False ),
        Room("Room description 1, 3",  False, True, True, False ),
        Room("Room description 2, 3",  True, True, False, True ),
        Room("Room description 3, 3",  False, True, False, True ),
        Room("Room description 4, 3",  True, False, True, False )
    ],
    [ 
        Room("Room description 0, 4",  True, True, False, False ),
        Room("Room description 1, 4",  True, False, False, True ),
        Room("Room description 2, 4",  False, False, False, False ),
        Room("Room description 3, 4",  True, False, False, False ),
        Room("Room description 4, 4",  True, False, False, False )
    ]
]


print("----------------------------------------")
x, y = 2, 2
print(rooms[y][x].description)

def move_player(direction_text, direction_index, x_inc, y_inc):
    """Checks if player can move towards a specific direction and moves him there
    
    Arguments:
        direction_text {string} -- Text with the direction the player wants to move

        direction_index {int} -- Number indicating direction (0 == North, 1 == East, 2 = South, 3 = West)

        x_inc {int} -- If movement is possible in the direction, how much to move on the X
        
        y_inc {int} -- If movement is possible in the direction, how much to move on the Y
    
    Returns:
        [bool] -- True if the command was processed, False otherwise
    """
    global x,y
    global rooms
    
    # Get the current room
    current_room = rooms[y][x]

    # Check if the player can move towards the given direction
    if (current_room.CanExit(direction_index)):
        # Write a message describing the action
        print("You move " + direction_text + "...")
        # Move the player
        x = x + x_inc
        y = y + y_inc
        # Update the current room
        current_room = rooms[y][x]
        # Write the new room's description
        print(current_room.description)
    else:
        # Write a message saying the player can't move
        print("You can't move " + direction_text)

    # Command was successfully processed
    return True

move_north = lambda : move_player("north", 0, 0, -1)
move_east = lambda : move_player("east", 1, 1, 0)
move_south = lambda : move_player("south", 2, 0, 1)
move_west = lambda : move_player("west", 3, -1, 0)

command_processor = {
    "north" : move_north,
    "n" : move_north,
    "east": move_east,
    "e": move_east,
    "south": move_south,
    "s": move_south,
    "west": move_west,
    "w": move_west
}

command = ""
while (command != "exit"):    
    print("")
    print("What now?")
    command = input()
    command = command.strip()
    if (command == ""):
        continue

    if (command in command_processor):
        command_processor[command]()
    elif (command == "exit"):
        break
    elif (command == "quit"):
        break
    else:
        print("I don't understand " + command + "!")
    
    print()

print("Goodbye...")
        
    