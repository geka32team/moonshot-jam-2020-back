"""Challenge level #4.
   Returns a task in form {"task": "a +/- x +/- c = d , a +/- b +/- x = d", "result": "x"}
"""
import random

def level_4_challenge():
    x_place_randomizer = random.randint(0, 2)
    a = random.randint(1, 5)
    b = random.randint(-5, 5)
    c = random.randint(-5, 9)

    d = a+b+c

    if b < 0:
        if c < 0:
            sign1 = '-'
            sign2 = '-'
            if x_place_randomizer == 0:
                x = a
                a_mod = 'x'
                b_mod = -b
                c_mod = -c
            if x_place_randomizer == 1:
                x = -b
                a_mod = a
                b_mod = 'x'
                c_mod = -c
            else:
                x = -c
                a_mod = a
                b_mod = -b
                c_mod = 'x'
        else:
            sign1 = '-'
            sign2 = '+'
            if x_place_randomizer == 0:
                x = a
                a_mod = 'x'
                b_mod = -b
                c_mod = c
            if x_place_randomizer == 1:
                x = -b
                a_mod = a
                b_mod = 'x'
                c_mod = c
            else:
                x = c
                a_mod = a
                b_mod = -b
                c_mod = 'x'
    else:
        if c < 0:
            sign1 = '+'
            sign2 = '-'
            if x_place_randomizer == 0:
                x = a
                a_mod = 'x'
                b_mod = b
                c_mod = -c
            if x_place_randomizer == 1:
                x = b
                a_mod = a
                b_mod = 'x'
                c_mod = -c
            else:
                x = -c
                a_mod = a
                b_mod = b
                c_mod = 'x'
        else:
            sign1 = '+'
            sign2 = '+'
            if x_place_randomizer == 0:
                x = a
                a_mod = 'x'
                b_mod = b
                c_mod = c
            if x_place_randomizer == 1:
                x = b
                a_mod = a
                b_mod = 'x'
                c_mod = c
            else:
                x = c
                a_mod = a
                b_mod = b
                c_mod = 'x'




    answer = " {} {} {} {} {} = {}".format(a_mod,sign1,b_mod,sign2,c_mod,d)
    return answer, x

print(level_4_challenge())