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

import getpass

from colorama import deinit, init

END = '\033[0m'
G = '\033[92m'
R = '\033[91m'

MSG_ASK1L = 'Player 1 - letter in word: '
MSG_ASK1W = 'Player 1 - word: '
MSG_ASK2 = 'Player 2 - missing letter: '


def ask(answer):
    if answer == ask1l:
        print(G + ask1w + END)

        exit()


if __name__ == '__main__':
    ask1w = getpass.getpass(MSG_ASK1W)
    ask1l = getpass.getpass(MSG_ASK1L)

    missing = ask1w.replace(ask1l, ' ')

    print(missing)

    init()

    ask2 = input(MSG_ASK2)

    ask(ask2)

    ask2 = input(MSG_ASK2)

    ask(ask2)

    print(R + ask1l + END)

    deinit()
