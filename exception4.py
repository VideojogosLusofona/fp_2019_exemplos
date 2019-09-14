class InvalidPosition(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def MoveNorth():
    # Do some calculations, but there was a problem, but we handled it
    raise InvalidPosition(15, 20)

# Main code
# Receive some input from the player, and then move north
try:
    MoveNorth()
except InvalidPosition as exp:
    print("Invalid position: " + str(exp.x) + "," + str(exp.y))
