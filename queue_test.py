from collections import deque

queue = deque()

print(queue)

if (queue):
   value = queue.pop()
   print("Removed " + str(value) + " from queue")
else:
   print("Queue was empty!")

print(queue)