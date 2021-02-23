"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""

import random

def test_level_2_challenge():
    a = random.randint(1, 3)
    b = random.randint(1, 5)
    c = a * b
    operation = random.randint(0, 1)

    if operation == 0:
        sign = '*'
        x = c
        assert (x == a*b and x >= 0 and a >= 0 and b >= 0)
    else:
        sign = '/'
        x = a
        a, c = c, a
        assert (x == a/b and x >= 0 and a >= b and b >= 0)







