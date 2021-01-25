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

chint = '*'

r_ans = random.choice(string.digits)

MSG_ANS = f'The answer was {r_ans}'
MSG_ASK = 'Guess the number (0-9) '
MSG_COR = ('\033[32m'
           'Correct!'
           '\033[0m')
MSG_INC = (f'\033[31m'
           f'Try again {chint}'
           '\033[0m')


def main():
    asint = int(r_ans)

    pop = string.digits

    init()

    for s in MSG_INC, MSG_INC, MSG_ANS:
        cursor_up = '\033[A'
        cursor_up_ask = f'{cursor_up}                       '

        while True:
            ans = input(MSG_ASK)

            if ans and ans in pop:
                break

            ans_sz = len(ans) * ' '

            line = f'{cursor_up_ask}{ans_sz}{cursor_up}'
            print(line)
            print()
            print()
            print(line, end='\r')

        if ans == r_ans:
            print(MSG_COR)

            return

        if s == MSG_INC:
            if int(ans) > asint:
                hint = '>'
            else:
                hint = '<'

            print(s.replace(chint, hint))
        else:
            print(s)

        pop = pop.replace(ans, '')

    deinit()


if __name__ == '__main__':
    main()
