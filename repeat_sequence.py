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

__all__ = []

import random
import time

from colorama import deinit, init

MSG_ASK = 'What was the sequence? '
MSG_CORRECT = '\033[32mCorrect!\033[0m'
MSG_INCORRECT = '\033[31mIncorrect\033[0m'


def main():
    k = 4

    lines = r'|\-/'

    seconds = 1

    init()

    while True:
        s = ''

        sequence = random.choices(lines, k=k)
        sequence = ''.join(sequence)

        for i in range(k):
            if not i:
                s = ''
            elif i == 1:
                s = ' '
            else:
                s = i * ' '

            print(s, sequence[i], end='\r')
            time.sleep(seconds)

        print(f'{s}  ')

        if input(MSG_ASK) == sequence:
            print(MSG_CORRECT)
        else:
            print(MSG_INCORRECT)
            break

    deinit()


if __name__ == '__main__':
    main()
