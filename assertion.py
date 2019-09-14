import math

def square_root(x):
    assert x >= 0, "Oh, oh, this should never happen, square_root wasn't supposed to be called with a negative number"
    return math.sqrt(x)

print(square_root(-16))

