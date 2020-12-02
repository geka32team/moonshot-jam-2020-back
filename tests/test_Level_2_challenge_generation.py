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
        assert (x == a*b)
    else:
        sign = '/'
        x = a
        a, c = c, a
        assert (x == a/b)

def test_level_2_challenge2():
    a = random.randint(1, 3)
    b = random.randint(1, 5)
    c = a * b
    operation = random.randint(0, 1)
    if operation == 0:
        sign = '*'
        x = c

    else:
        sign = '/'
        x = a
        a, c = c, a

    assert (x >= 0)

def test_level_2_challenge3():
    a = random.randint(1, 3)
    b = random.randint(1, 5)
    c = a * b
    operation = random.randint(0, 1)
    if operation == 0:
        sign = '*'
        x = c
        assert (a >= 0 and b >= 0)

    else:
        sign = '/'
        x = a
        a, c = c, a
        assert (a >= b and b >= 0)






