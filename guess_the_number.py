# MIT License

# Copyright (c) 2021 Joao Ferreira

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
The user has three attempts to guess what number was chosen at random

Non-digits are not accepted
Digits accepted are removed from the pool
"""

import random
import string

from colorama import deinit, init

hint = '*'

r_a = random.choice(string.digits)

A = '\033[A'
A_ASK = f'{A}                       '

MSG_ANS = f'The answer was {r_a}'
MSG_ASK = 'Guess the number (0-9) '
MSG_COR = ('\033[32m'
           'Correct!'
           '\033[0m')
MSG_INC = (f'\033[31m'
           f'Try again {hint}'
           '\033[0m')


def main():
    i = int(r_a)

    pop = string.digits

    init()

    for m in MSG_INC, MSG_INC, MSG_ANS:
        while True:
            a = input(MSG_ASK)

            if a and a in pop:
                break

            a_sz = len(a) * ' '

            s = f'{A_ASK}{a_sz}{A}'
            print(s)
            print()
            print()
            print(s, end='\r')

        if a == r_a:
            print(MSG_COR)
            return

        if m == MSG_INC:
            if int(a) > i:
                h = '>'
            else:
                h = '<'
            print(m.replace(hint, h))
        else:
            print(m)

        pop = pop.replace(a, '')

    deinit()


if __name__ == '__main__':
    main()
