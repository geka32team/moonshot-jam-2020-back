"""Challenge level #2.
   Returns a task in form {"task": "a (*)/ b = ?", "result": "x"}
"""
import random

def level_2_challenge():
    a = random.randint(1, 3)
    b = random.randint(1, 5)
    c = a*b
    operation = random.randint(0, 1)

    if operation == 0 :
        sign = '*'
        x = c
    else:
        sign = '/'
        x = a
        a, c = c, a

    answer = " {} {} {} = ?".format(a,sign,b)
    return answer, x

print(level_2_challenge())

