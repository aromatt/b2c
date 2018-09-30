#!/usr/bin/env python2

from __future__ import print_function
from datetime import datetime
import random
import sys
from b2c import *

if len(sys.argv) > 1:
    iterations = int(sys.argv[1])
else:
    iterations = 10000

print("Trying {} boards".format(iterations))
random.seed(datetime.now())
max_board = None
max_score = 0
tried_boards = set()
for i in range(iterations):
    if i % 5000 == 0:
        print('boards done: {}; max score: {}'.format(i, max_score))
        sys.stdout.flush()
    board = build_board()
    score = score_board(board)
    if score > max_score:
        max_score = score
        max_board = board
        print("\nbest board ({}):".format(max_score))
        print(board_str(max_board))


print("\n\nfinal best board ({}):".format(max_score))
print(board_str(max_board))
