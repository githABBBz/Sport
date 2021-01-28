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

chosen = random.choice(string.digits)

ASK = '                       '
CURSOR_UP = '\033[A'

HINT = '*'

MSG_ANSWER = f'The answer was {chosen}'
MSG_ASK = 'Guess the number (0-9) '
MSG_CORRECT = ('\033[32m'
               'Correct!'
               '\033[0m')
MSG_INCORRECT = ('\033[31m'
                 f'Try again {HINT}'
                 '\033[0m')


def main():
    chosen_as_int = int(chosen)

    digits = string.digits

    init()

    for msg in MSG_INCORRECT, MSG_INCORRECT, MSG_ANSWER:
        while True:
            digit = input(MSG_ASK)

            if digit and digit in digits:
                break

            length = len(digit)

            if not length:
                s = ''
            elif length == 1:
                s = ' '
            else:
                s = length * ' '

            ask = f'{CURSOR_UP}{ASK}{s}{CURSOR_UP}'
            print(ask)
            print()
            print()
            print(ask, end='\r')

        if digit == chosen:
            print(MSG_CORRECT)
            break

        if msg == MSG_INCORRECT:
            if int(digit) > chosen_as_int:
                hint = '>'
            else:
                hint = '<'
            print(msg.replace(HINT, hint))
        else:
            print(msg)

        digits = digits.replace(digit, '')

    deinit()


if __name__ == '__main__':
    main()
