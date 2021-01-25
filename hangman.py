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

import getpass

from colorama import deinit, init

END = '\033[0m'
GRE = '\033[32m'
RED = '\033[31m'

MSG_ASK1L = 'Player 1 - Letter in word: '
MSG_ASK1W = 'Player 1 - Word: '
MSG_ASK2 = 'Player 2 - Missing letter: '

TRY = 2

ask1w = getpass.getpass(MSG_ASK1W)
ask1l = getpass.getpass(MSG_ASK1L)

missing = '?'
missing = ask1w.replace(ask1l, missing)

print(missing)

init()

for _ in range(TRY):
    ask2 = input(MSG_ASK2)

    if ask2 == ask1l:
        print(f'{GRE}{ask1w}{END}')
        break
else:
    print(f'{RED}{ask1l}{END}')

deinit()
