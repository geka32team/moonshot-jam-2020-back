
"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""

import math
import random

def get_limits(lvl):

    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    min = 3
    max = 6

    deca = math.floor(lvl/10)

    for i in range(math.ceil(lvl/10)):
        min += fib[i] * (10 if deca else lvl%10)
        max += fib[i + 2] * (10 if deca else lvl%10)
        deca -= 1

    return [min, max]


def level_1_challenge(level):
    limits = get_limits(level)
    min = limits[0]
    max = limits[1]
    randomizer = random.randint(0, 1)

    a = random.randint(min, max)
    b = random.randint(min, max)

    if randomizer == 0:
        sign = '+'
        x = a + b
    else:
        sign = '-'
        if b > a:
            a, b = b, a
        if b == a:
            a += 1
        a = int(a * 1.3)
        x = a - b


    answer = "{} {} {} = ?".format(a, sign, b)
    return answer, x,

