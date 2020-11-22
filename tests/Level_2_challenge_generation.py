"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""
import random

a = random.randint(0, 3)
b = random.randint(1, 5)
c = a*b
operation = random.randint(0, 1)

if operation == 0 :
    sign = '*'
    x = c
else :
    sign = '/'
    x = a
    a, c = c, a

answer = int(input(" {} {} {} = ?\n".format(a,sign,b)))

if answer == x :
    print("Well Done")
else :
    print("Answer not correct")

