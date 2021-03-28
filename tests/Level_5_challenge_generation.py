"""Challenge level #5.
   Returns a task in form {"task": "a+(b -X + c) = 6", "result": "x"}
"""
import random
from Level_1_challenge_generation import get_limits as get_lim

def level_5_challenge(level):
    randomizer = random.randint(0, 7)
    brackets_randomizer = random.randint(0, 2)
    x_place_randomizer = random.randint(0, 3)
    limits = get_lim(level)
    min = limits[0]
    max = limits[1]

    a = random.randint(min, max)
    b = random.randint(min, max)
    c = random.randint(min, max)
    d = random.randint(min, max)

    if randomizer == 0:
        sign1 = '+'
        sign2 = '+'
        sign3 = '+'
        e = a + b + c + d
    elif randomizer == 1:
        sign1 = '+'
        sign2 = '+'
        sign3 = '-'
        e = a + b + c - d
        if e < 0:
            e, d = d, -e
            sign3 = '+'
    elif randomizer == 2:
        sign1 = '+'
        sign2 = '-'
        sign3 = '+'
        e = a + b - c + d
        if e < 0:
            e, c = c, -e
            sign2 = '+'
    elif randomizer == 3:
        sign1 = '+'
        sign2 = '-'
        sign3 = '-'
        e = a + b - c + d
        if e < 0:
            e, c = c, -e
            sign2 = '+'
    elif randomizer == 4:
        sign1 = '-'
        sign2 = '+'
        sign3 = '+'
        e = a - b + c + d
        if e < 0:
            e, b = b, -e
            sign1 = '+'
    elif randomizer == 5:
        sign1 = '-'
        sign2 = '-'
        sign3 = '+'
        e = a - b + c + d
        if e < 0:
            e, b = b, -e
            sign1 = '+'
    elif randomizer == 6:
        sign1 = '-'
        sign2 = '+'
        sign3 = '-'
        e = a - b + c + d
        if e < 0:
            e, b = b, -e
            sign1 = '+'
    elif randomizer == 7:
        sign1 = '-'
        sign2 = '-'
        sign3 = '-'
        e = a - b + c + d
        if e < 0:
            e, b = b, -e
            sign1 = '+'

    if x_place_randomizer == 0:
        x = a
        a_mod = 'x'
        b_mod = b
        c_mod = c
        d_mod = d
    elif x_place_randomizer == 1:
        x = b
        a_mod = a
        b_mod = 'x'
        c_mod = c
        d_mod = d
    elif x_place_randomizer == 2:
        x = c
        a_mod = a
        b_mod = b
        c_mod = 'x'
        d_mod = d
    else:
        x = d
        a_mod = a
        b_mod = b
        c_mod = c
        d_mod = 'x'

    if brackets_randomizer == 0:
        answer = " ({} {} {}) {} {} {} {} = {}".format(a_mod, sign1, b_mod, sign2, c_mod, sign3, d_mod, e)
    elif brackets_randomizer == 1:
        if sign1 == "-" and sign2 == "+":
            sign2 = "-"

        answer = " {} {} ({} {} {}) {} {} = {}".format(a_mod, sign1, b_mod, sign2, c_mod, sign3, d_mod, e)
    elif brackets_randomizer == 2:
        if sign2 == "-" and sign3 == "+":
            sign3 = "-"

        answer = " {} {} {} {} ({} {} {}) = {}".format(a_mod, sign1, b_mod, sign2, c_mod, sign3, d_mod, e)
    elif brackets_randomizer == 3:
        if sign1 == "-" and sign2 == "+":
            sign2 = "-"
        if sign1 == "-" and sign3 == "+":
            sign3 = "-"

        answer = " {} {} ({} {} {} {} {}) = {}".format(a_mod, sign1, b_mod, sign2, c_mod, sign3, d_mod, e)
    elif brackets_randomizer == 4:

        answer = " ({} {} {} {} {}) {} {} = {}".format(a_mod, sign1, b_mod, sign2, c_mod, sign3, d_mod, e)

    return answer, x


print(level_5_challenge(5))
