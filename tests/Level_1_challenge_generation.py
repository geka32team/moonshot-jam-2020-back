
"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""


import random

def level_1_challenge(level):

    if level <= 10:
        a = random.randint(level+4, (2*level+8))
        b = random.choice([*range(-(2*level+4)-(level+2)), *range(level+2),(2*level+4)])
    elif level > 10 and level <= 20:
        a = random.randint(level+4, (2*level+9))
        b = random.choice([*range(-(2*level+5),-(level+2)), *range(level+2, (2*level+5))])
    else:
        a = random.randint((2*level+3), (2*level+9))
        b = random.choice([*range(-(2*level+5),-(level+2)), *range(level+2, (2*level+6))])
    if b < 0:
        sign = '-'
    else:
        sign = '+'
    if a + b == 0:
        a += 1
    if sign == '-' and abs(b) > a :
        a, b = b, a
    x = abs(a+b)
    answer = "{} {} {} = ?".format(abs(a),sign,abs(b))
    return answer, x, a, b



print(level_1_challenge(19))
