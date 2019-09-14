class InvalidPosition(Exception):
    pass


def MoveNorth():
    # Do some calculations, but there was a problem, but we handled it
    raise InvalidPosition

# Main code
# Receive some input from the player, and then move north
try:
    MoveNorth()
except InvalidPosition:
    print("Invalid position!")
