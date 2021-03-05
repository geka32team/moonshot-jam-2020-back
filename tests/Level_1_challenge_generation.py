
"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""


import random

def level_1_challenge(level):

    if level <= 10:
        a = random.randint((level+4), (2*level+8))
        b = random.choice([*range(-(2*level+4),-(level+1)), *range((level+2),(2*level+5))])
    elif level > 10 and level <= 20:
        a = random.randint((level+4), (3*level+7))
        b = random.choice([*range(-(3*level+3),-(level+1)), *range((level+2), (3*level+4))])
    else:
        a = random.randint((2*level+3), (5*level+5))
        b = random.choice([*range(-(5*level-3),-(2*level+3)), *range((2*level+4), (5*level-2))])

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

