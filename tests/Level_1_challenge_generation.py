
"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""


import random

def level_1_challenge(level):
    a = random.randint(level-3, level+3)
    b = random.choice([*range(-(level+3),-level), *range(level, level+3)])
    if b < 0:
        sign = '-'
    else:
        sign = '+'
    if a + b == 0:
        a += 1
        print("ooh la la")
    if sign == '-' and abs(b) > a :
        a, b = b, a
    x = abs(a+b)
    answer = "{} {} {} = ?".format(abs(a),sign,abs(b))
    return answer, x, a, b



print(level_1_challenge(85))
