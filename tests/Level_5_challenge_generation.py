"""Challenge level #5.
   Returns a task in form {"task": "a+(b -X + c) = 6", "result": "x"}
"""
import random


def level_5_challenge():
    braces_place_randomizer = random.randint(0, 2)
    three_numbers_in_braces = random.randint(0, 1)
    x_place_randomizer = random.randint(0, 3)

    braces_place_randomizer = 0

    if braces_place_randomizer == 0:
        braces1 = "("
        braces2 = ")"
        if three_numbers_in_braces == 1:
            m = random.randint(0, 5)
            n = random.randint(-5, 5)
            o = random.randint(-5, 5)
            if sum((m, n, o)) < 0:
                if n < 0:
                    m, n, o = -n, -m, -o
                elif o < 0:
                    m, n, o = -o, -n, -m
            a = m + n + o
            if n < 0:
                braces_sign1 = "-"
            else:
                braces_sign1 = "+"
            if o < 0:
                braces_sign2 = "-"
            else:
                braces_sign2 = "+"

            a_mod = "({} {} {} {} {})".format(m, braces_sign1, abs(n), braces_sign2, abs(o))
            b = random.randint(-5, 5)
            c = 0
        else:
            m = random.randint(0, 5)
            n = random.randint(-5, 5)
            if sum((m, n)) < 0:
                m, n = -n, -m
            a = m + n
            if n < 0:
                braces_sign1 = "-"
            else:
                braces_sign1 = "+"

            a_mod = "({} {} {})".format(m, braces_sign1, abs(n))
            b = random.randint(-5, 5)
            b = random.randint(-5, 5)
            c = random.randint(-5, 5)
    elif braces_place_randomizer == 1:
        if three_numbers_in_braces == 1:
            a = random.randint(0, 5)
            m = random.randint(0, 5)
            n = random.randint(-5, 5)
            o = random.randint(-5, 5)
            c = 0
        else:
            a = random.randint(0, 5)
            m = random.randint(0, 5)
            n = random.randint(-5, 5)
            c = random.randint(-5, 5)
    elif braces_place_randomizer == 2:
        if three_numbers_in_braces == 1:
            a = random.randint(0, 5)
            m = random.randint(0, 5)
            n = random.randint(-5, 5)
            o = random.randint(-5, 5)
            o = m + n + o
            b = 0
        else:
            a = random.randint(0, 5)
            b = random.randint(-5, 5)
            m = random.randint(0, 5)
            n = random.randint(-5, 5)
            c = m + n






    d = a + b + c



    answer = " {} {} {} {} {} = {}".format( a_mod  , a_mod, a_mod, a_mod, a_mod, a_mod ,a_mod, a_mod, a_mod, d)
    return answer, a


print(level_5_challenge())
