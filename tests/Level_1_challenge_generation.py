
"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""


import random

def level_1_challenge():
    a = random.randint(0, 9)
    b = random.randint(-5, 5)
    if b < 0 :
        sign = '-'
    else :
        sign = '+'

    if sign == '-' and abs(b) > a :
        a, b = b, a
    x = abs(a+b)
    answer = "{} {} {} = ?".format(abs(a),sign,abs(b))
    return answer, x


print(level_1_challenge())
