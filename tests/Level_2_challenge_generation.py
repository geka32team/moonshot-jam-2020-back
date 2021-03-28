"""Challenge level #2.
   Returns a task in form {"task": "a (*)/ b = ?", "result": "x"}
   OR
   Returns a task in form {"task": "a +/-x = c"  or "x +/-b = c" or "a +/- b = x", "result": "x"}
"""
import math
import random
from Level_1_challenge_generation import get_limits as get_lim

def get_limits(lvl):

    fib = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    min = 1
    max = 2

    deca = lvl//12

    for i in range(math.ceil(lvl/12)):
        rest = lvl%12
        min += fib[i] * (4 if deca else rest//3)
        max += fib[i + 3] * (4 if deca else rest//3)
        if(rest%3 == 1):
            max += 1
        elif (rest%3 == 2):
            max += 2

        deca -= 1


    return [min, max]


def level_2_challenge_1(level):
    limits = get_limits(level)
    min = limits[0]
    max = limits[1]

    a = random.randint(min, max)
    b = random.randint(min, max)
    c = a * b
    operation = random.randint(0, 1)

    if operation == 0:
        sign = '*'
        x = c
    else:
        sign = '/'
        x = a
        a, c = c, a

    answer = " {} {} {} = ?".format(a, sign, b)
    return answer, x

def level_2_challenge_2(level):
    randomizer = random.randint(0, 1)
    x_place_randomizer = random.randint(0, 2)
    limits = get_lim(level)
    min = limits[0]
    max = limits[1]

    a = random.randint(min, max)
    b = random.randint(min, max)


    if randomizer == 0:
        sign = '+'
        c = a + b
    else:
        sign = '-'
        if b > a:
            a, b = b, a
        if b == a:
            a += 1
        a = int(a * 1.3)
        c = a - b

    if x_place_randomizer == 0:
        x = a
        answer = " x {} {} = {}".format(sign, b, c)
    elif x_place_randomizer == 1:
        x = b
        answer = " {} {} x = {}".format(a,sign, c)
    else:
        x = c
        answer = " {} {} {} = x".format(a, sign, b)




    return answer, x

def level_2_challenge(level):
    return level_2_challenge_2(level) if random.randint(0, 1) else level_2_challenge_1(level)

print(level_2_challenge(2))