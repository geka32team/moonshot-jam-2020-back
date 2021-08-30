"""Challenge level #1.
   Returns a task in form {"task": "a +/- b = ?", "result": "x"}
"""

import random
from Limits import Limits

class Level1:
    def __init__(self, level):
        self.level = level
    def level_1_challenge(self):
        limits_object = Limits(self.level)
        limits = limits_object.get_limits()
        minimum = limits[0]
        maximum = limits[1]
        sign = random.choice(['-', '+'])

        a = random.randint(minimum, maximum)
        b = random.randint(minimum, maximum)

        if sign == '+':
            x = a + b
        else:
            if b > a:
                a, b = b, a
            a = int(a * 1.3)
            x = a - b


        answer = "{} {} {} = ?".format(a, sign, b)
        return answer, x

test = Level1(1)
print(test.level_1_challenge())
