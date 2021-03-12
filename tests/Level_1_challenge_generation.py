
"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""

import math
import random

def count_limits(level):

    dict = {
        "m1": 1,
        "n1": 2,
        "m2": 1,
        "n2": 3,
        "m3": 2,
        "n3": 5
    }

    dec = ((math.floor(level/10)) * 10)

    if level <= 10:
        min = (dict.get("m1") * level)
        max = (dict.get("n1") * level)
    elif level > 10 and level <= 20:
        min = ((dict.get("m1") * 10) + (dict.get("m2") * (level - dec)))
        max = ((dict.get("n1") * 10) + (dict.get("n2") * (level - dec)))
    else:
        min = ((dict.get("m1") * 10) + (dict.get("m2") * 10) + (dict.get("m3") * (level - dec)))
        max = ((dict.get("n1") * 10) + (dict.get("n2") * 10) + (dict.get("n3") * (level - dec)))

    return [min, max]


def level_1_challenge(level):

    a = random.randint(count_limits(level)[0]+4, count_limits(level)[1] + 8)
    b = random.choice([*range((-count_limits(level)[1]) - 4,(-count_limits(level)[0]) - 3), *range((count_limits(level)[0] + 2), (count_limits(level)[1]) + 5)])

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

