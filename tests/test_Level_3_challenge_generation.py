"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""

import random

def test_level_3_challenge():
    x_place_randomizer = random.randint(0, 1)
    a = random.randint(1, 9)
    b = random.randint(-5, 5)

    if b < 0:
        sign = '-'
        if x_place_randomizer == 0:
            x = a
            a_mod = 'x'
            b_mod = -b
        else:
            x = -b
            a_mod = a
            b_mod = 'x'

        if sum((a, b)) < 0:
            a, b = b, a

    else:
        sign = '+'
        if x_place_randomizer == 0:
            x = a
            a_mod = 'x'
            b_mod = b
        else:
            x = b
            a_mod = a
            b_mod = 'x'
    c = a + b

    answer = " {} {} {} = {}".format(a_mod, sign, b_mod, abs(c))

    return answer, x

    assert x >= 0 and a >= 0 and c >=0