"""A class generates integer limits based on level using Fibonacci sequence. Limits will be used for integers generation in our math tasks"""

import math

class Limits:
    def __init__(self, lvl):
        self.lvl = lvl
    def get_limits(self):

        fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        min = 3
        max = 6

        deca = math.floor(self.lvl/10)

        for i in range(math.ceil(self.lvl/10)):
            min += fib[i] * (10 if deca else self.lvl%10)
            max += fib[i + 2] * (10 if deca else self.lvl%10)
            deca -= 1

        return [min, max]