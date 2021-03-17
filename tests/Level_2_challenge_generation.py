"""Challenge level #2.
   Returns a task in form {"task": "a (*)/ b = ?", "result": "x"}
   OR
   Returns a task in form {"task": "a +/-x = c"  or "x +/-b = c", "result": "x"}
"""
import math
import random

def get_limits(lvl):

    fib = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    min = 1
    max = 2

    deca = math.floor(lvl/12)

    for i in range(math.ceil(lvl/12)):
        rest = lvl%12
        min += fib[i] * (4 if deca else math.floor(rest/3))
        max += fib[i + 3] * (4 if deca else math.floor(rest/3))
        if(rest%3 == 1):
            max += 1
        elif (rest%3 == 2):
            max += 2

        deca -= 1
    print([min, max]);

    return [min, max]


def level_2_challenge(level):
    limits = get_limits(level)
    min = limits[0]
    max = limits[1]

    a = random.randint(min, max)
    b = random.randint(min, max)
    x = a + b

    if random.randint(0, 1) :
        sign = '-'
        if b > a :
            a, b = b, a
        a = int(a * 1.3)
        x = a - b
    else:
        sign = '+'

    answer = "{} {} {} = ?".format(a, sign, b)
    return answer, x,

print(level_2_challenge(23))
print(level_2_challenge(24))
print(level_2_challenge(25))
print(level_2_challenge(26))
print(level_2_challenge(27))