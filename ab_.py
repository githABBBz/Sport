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

"""Hit the next letter"""

import getpass
import queue
import string
import threading
import time

from colorama import deinit, init

_A = '\033[A'

BREAK = 0.1


def hit(put):
    s = getpass.getpass('')
    put(s)


q = queue.Queue()

t = threading.Thread(args=(q.put,), daemon=True, target=hit)

t.start()

init()

for char in string.ascii_lowercase:
    if not q.empty():
        z = q.get()

        if z and z in string.ascii_lowercase:
            print(_A + z + _A)
            print()

            break
    print(char)

    time.sleep(BREAK)

deinit()

timeout = 0.1

t.join(timeout)
