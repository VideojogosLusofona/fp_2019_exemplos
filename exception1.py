class InvalidPosition(Exception):
    pass


def MoveNorth():
    # Do some calculations, but there was a problem
    raise InvalidPosition

# Main code
# Receive some input from the player, and then move north
MoveNorth()

