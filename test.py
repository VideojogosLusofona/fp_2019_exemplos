def max_incorrect(a,b,c):
    if (a > b):
        if (a > c):
            return a
        else:
            return c
    else:
        if (b > c):
            return b
        else:
            return c

result = max_incorrect(5,2,9)
print("Max Incorrect = " + str(result))


