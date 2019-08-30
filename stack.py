from collections import deque

stack = deque()

print(stack)

if (stack):
    value = stack.pop()
    print("Removed " + str(value) + " from stack")
else:
    print("Stack was empty!")

print(stack)
