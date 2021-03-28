"""Challenge level #4.
   Returns a task in form {"task": "(a +/- x) +/- c = d , a +/- (b +/- x) = d", "result": "x"}
"""
import random
from Level_1_challenge_generation import get_limits as get_lim

def level_4_challenge(level):
    randomizer = random.randint(0, 3)
    brackets_randomizer = random.randint(0, 1)
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
        a_mod = 'x'
        b_mod = b
        c_mod = c
    elif x_place_randomizer == 1:
        x = b
        a_mod = a
        b_mod = 'x'
        c_mod = c
    else:
        x = c
        a_mod = a
        b_mod = b
        c_mod = 'x'

    if brackets_randomizer == 0:
        answer = " ({} {} {}) {} {} = {}".format(a_mod, sign1, b_mod, sign2, c_mod, d)
    else:
        if sign1 == "-" and sign2 == "+":
            sign2 = "-"

        answer = " {} {} ({} {} {}) = {}".format(a_mod, sign1, b_mod, sign2, c_mod, d)

    return answer, x

print(level_4_challenge(2))



