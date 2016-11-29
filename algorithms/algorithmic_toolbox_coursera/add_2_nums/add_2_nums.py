# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

import sys

input_val = sys.stdin.read()
tokens = input_val.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)