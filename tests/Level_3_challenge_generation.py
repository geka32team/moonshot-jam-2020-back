"""Challenge level #3.
   Returns a task in form {"task": "x +/- b +/- c = d","a +/- x +/- c = d , a +/- b +/- x = d", "result": "x"}
"""
import random
from Level_1_challenge_generation import get_limits as get_lim

def level_3_challenge(level):

    randomizer = random.randint(0, 3)
    x_place_randomizer = random.randint(0, 2)
    limits = get_lim(level)
    min = limits[0]
    max = limits[1]

    a = random.randint(min, max)
    b = random.randint(min, max)
    c = random.randint(min, max)

    if randomizer == 0:
        sign1 = '+'
        sign2 = '+'
        d = a + b + c

    elif randomizer == 1:
        sign1 = '+'
        sign2 = '-'
        d = a + b - c
        if d < 0:
            d, c = c, -d
            sign2 = '+'

    elif randomizer == 2:
        sign1 = '-'
        sign2 = '+'
        d = a - b + c
        if d < 0:
            d, b = b, -d
            sign1 = '+'

    elif randomizer == 3:
        sign1 = '-'
        sign2 = '-'
        d = a - b - c
        if d < 0:
            d, b = b, -d
            sign1 = '+'


    if x_place_randomizer == 0:
        x = a
        answer = " x {} {} {} {} = {}".format(sign1, b, sign2, c, d)
    elif x_place_randomizer == 1:
        x = b
        answer = " {} {} x {} {} = {}".format(a, sign1, sign2, c, d)
    else:
        x = c
        answer = " {} {} {} {} x = {}".format(a, sign1, b, sign2, d)

    return answer, x

print(level_3_challenge(2))