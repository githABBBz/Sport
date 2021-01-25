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

"""The user has three attempts to guess what number was chosen at random"""

__all__ = []

import random
import string

from colorama import deinit, init

right_answer = random.choice(string.digits)

as_int = int(right_answer)

MSG_ANS = 'The answer was ' + right_answer
MSG_ASK = 'Guess the number (0-9) '
MSG_OK = '\033[92mCorrect!\033[0m'
MSG_TRY = '\033[91mTry again *\033[0m'


def ask(addline, msg_wrong):
    """
    One attempt

    Non-digits are not accepted

    Digits accepted are removed from the pool
    and are not accepted in subsequent attempts
    """
    global pool

    cursor_up = '\033[A'

    cursor_up_ask = cursor_up + '                       '

    while True:
        answer = input(MSG_ASK)

        if answer and answer in pool:
            break

        answer_sz = len(answer)
        answer_sz = answer_sz * ' '

        line = cursor_up_ask + answer_sz + cursor_up

        print(line)

        print()

        if addline:
            print()

        print(line, end='\r')

    if answer == right_answer:
        print(MSG_OK)

        exit()

    if msg_wrong == MSG_TRY:
        i = int(answer)

        if i > as_int:
            hint = '>'
        else:
            hint = '<'

        msg_wrong = msg_wrong.replace('*', hint)

    print(msg_wrong)

    pool = pool.replace(answer, '')


if __name__ == '__main__':
    pool = string.digits

    init()

    ask(True, MSG_TRY)

    ask(True, MSG_TRY)

    ask(True, MSG_ANS)

    deinit()
