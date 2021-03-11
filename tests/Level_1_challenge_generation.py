
"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""

import math
import random

def level_1_challenge(level):


    dict = {
        "m1": 1,
        "n1": 2,
        "m2": 1,
        "n2": 3,
        "m3": 5,
        "n3": 2
    }

    amin1 = math.floor(dict.m1 * level)+4
    amax1 = math.floor(dict.n1 * level)+8


    if level <= 10:
        a = random.randint(amin1, amax1)
        b = random.choice([*range(-(2*level+4),-(level+1)), *range((level+2),(2*level+5))])
    elif level > 10 and level <= 20:
        a = random.randint((level+4), (3*level+7))
        b = random.choice([*range(-(3*level+3),-(level+1)), *range((level+2), (3*level+4))])
    else:
        a = random.randint((2*level+3), (5*level+6)-2*level)
        b = random.choice([*range(-(5*level+1),level-(2*level)), *range((2*level+1), (5*level+2)-level)])
    print(a, b)
    if b < 0 :
        sign = '-'
    else:
        sign = '+'
    if a + b == 0:
        a += 1
    if sign == '-' and abs(b) > a :
        a, b = b, a

    if sign == '-' :
        a = int(a * 1.3)
    x = abs(a+b)
    answer = "{} {} {} = ?".format(abs(a),sign,abs(b))
    return answer, x,

print(level_1_challenge(1))

