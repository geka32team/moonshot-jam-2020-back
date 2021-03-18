"""Challenge level #2.
   Returns a task in form {"task": "a (*)/ b = ?", "result": "x"}
   OR
   Returns a task in form {"task": "a +/-x = c"  or "x +/-b = c", "result": "x"}
"""
import math
import random

def get_limits_1(lvl):

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


    return [min, max]

def get_limits_2(lvl):

    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    min = 3
    max = 6

    deca = math.floor(lvl/10)

    for i in range(math.ceil(lvl/10)):
        min += fib[i] * (10 if deca else lvl%10)
        max += fib[i + 2] * (10 if deca else lvl%10)
        deca -= 1

    return [min, max]

def level_2_challenge_1(level):
    limits = get_limits_1(level)
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
    limits = get_limits_2(level)
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

    answer = " {} {} {} = {}".format(a_mod, sign, b_mod, c_mod)

    return answer, x

def level_2_challenge(level):
    randomizer = random.randint(0, 1);
    if randomizer == 0:
        return level_2_challenge_1(level)
    else:
        return level_2_challenge_2(level)

print(level_2_challenge(1))
print(level_2_challenge(2))
print(level_2_challenge(3))
print(level_2_challenge(4))