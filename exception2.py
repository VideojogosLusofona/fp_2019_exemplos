class InvalidPosition(Exception):
    pass


def MoveNorth():
    # Do some calculations, but there was a problem, but we handled it
    try:
        raise InvalidPosition
    except InvalidPosition:
        print("Invalid position!")

# Main code
# Receive some input from the player, and then move north
MoveNorth()

