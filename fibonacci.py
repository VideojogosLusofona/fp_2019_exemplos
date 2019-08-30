
def fibonacci(value):
    if (value < 2):
      return value

    return fibonacci(value - 2) + fibonacci(value - 1)

for i in range(0, 15):
    print(fibonacci(i))