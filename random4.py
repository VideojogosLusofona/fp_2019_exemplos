import random

choices = [ "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]

for i in range(0, 10):
    random.shuffle(choices)
    print(choices)
    