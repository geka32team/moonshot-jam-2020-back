
"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""

import math
import random

def level_1_challenge(level):


    dict = {
        "m1": 1,
        "n1": 2,
        "m2": 1,
        "n2": 3,
        "m3": 2,
        "n3": 5
    }

    amin1 = dict.get("m1") * level + 4
    amax1 = dict.get("n1") * level + 8
    bmin1 = dict.get("m1") * level + 2
    bmax1 = dict.get("n1") * level + 4

    amin2 = ((dict.get("m1") * 10) + (dict.get("m2") * (level-10))) + 4
    amax2 = ((dict.get("n1") * 10) + (dict.get("n2") * (level-10))) + 8
    bmin2 = ((dict.get("m1") * 10) + (dict.get("m2") * (level-10))) + 2
    bmax2 = ((dict.get("n1") * 10) + (dict.get("n2") * (level-10))) + 4

    amin3 = ((dict.get("m1") * 10) + (dict.get("m2") * 10) + (dict.get("m3") * (level-20))) + 4
    amax3 = ((dict.get("n1") * 10) + (dict.get("n2") * 10) + (dict.get("n3") * (level-20))) + 8
    bmin3 = ((dict.get("m1") * 10) + (dict.get("m2") * 10) + (dict.get("m3") * (level-20))) + 2
    bmax3 = ((dict.get("n1") * 10) + (dict.get("n2") * 10) + (dict.get("n3") * (level-20))) + 4


    if level <= 10:
        a = random.randint(amin1, amax1)
        b = random.choice([*range(-bmax1,-bmin1 + 1), *range(bmin1, bmax1 + 1)])
    elif level > 10 and level <= 20:
        a = random.randint(amin2, amax2)
        b = random.choice([*range(-bmax2,-bmin2 + 1), *range(bmin2, bmax2 + 1)])
    else:
        a = random.randint(amin3, amax3)
        b = random.choice([*range(-bmax3,-bmin3 + 1), *range(bmin3, bmax3 + 1)])
    print(a, b)
    if b < 0 :
        sign = '-'
    else:
        sign = '+'
    if a + b == 0:
        a += 1
    if sign == '-' and abs(b) > a :
        a, b = b, a

    if sign == '-' :
        a = int(a * 1.3)
    x = abs(a+b)
    answer = "{} {} {} = ?".format(abs(a),sign,abs(b))
    return answer, x,

print(level_1_challenge(21))

