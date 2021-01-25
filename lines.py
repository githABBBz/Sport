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

"""Repeat the sequence game"""

__all__ = []

import random
import time

from colorama import deinit, init

INTERVAL = 1

K = 4

POP = r'|\-/'

if __name__ == '__main__':
    init()

    while True:
        sequence = random.choices(POP, k=K)
        sequence = ''.join(sequence)

        # Question
        print('', sequence[0], end='\r')
        time.sleep(INTERVAL)

        print(' ', sequence[1], end='\r')
        time.sleep(INTERVAL)

        print('  ', sequence[2], end='\r')
        time.sleep(INTERVAL)

        print('   ', sequence[3], end='\r')
        time.sleep(INTERVAL)

        print('     ')

        # Answer
        repeat = input('What was the sequence? ')

        if repeat == sequence:
            print('\033[92mCorrect!\033[0m')
        else:
            print('\033[91mIncorrect\033[0m')

            break

    deinit()
