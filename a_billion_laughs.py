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

from colorama import deinit, init

MSG_A_BILLION_LAUGHS = '''ha0 = 'ha'
ha1 = ha0, ha0, ha0, ha0, ha0, ha0, ha0, ha0, ha0, ha0
ha2 = ha1, ha1, ha1, ha1, ha1, ha1, ha1, ha1, ha1, ha1
ha3 = ha2, ha2, ha2, ha2, ha2, ha2, ha2, ha2, ha2, ha2
ha4 = ha3, ha3, ha3, ha3, ha3, ha3, ha3, ha3, ha3, ha3
ha5 = ha4, ha4, ha4, ha4, ha4, ha4, ha4, ha4, ha4, ha4
ha6 = ha5, ha5, ha5, ha5, ha5, ha5, ha5, ha5, ha5, ha5
ha7 = ha6, ha6, ha6, ha6, ha6, ha6, ha6, ha6, ha6, ha6
ha8 = ha7, ha7, ha7, ha7, ha7, ha7, ha7, ha7, ha7, ha7
ha9 = ha8, ha8, ha8, ha8, ha8, ha8, ha8, ha8, ha8, ha8

\033[31mha9\033[0m'''

init()
print(MSG_A_BILLION_LAUGHS)
deinit()
