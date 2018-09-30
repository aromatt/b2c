#!/usr/bin/env python

from __future__ import print_function
from datetime import datetime
import random
import sys
from b2c import *

def print_status(board, score):
    print("\nbest board ({}):".format(score))
    print("  shops: {} pts".format(score_shops(board)))
    print("  factories: {} pts".format(score_factories(board)))
    print("  taverns: {} pts".format(score_taverns(board)))
    print("  offices: {} pts".format(score_offices(board)))
    print("  parks: {} pts".format(score_parks(board)))
    print("  houses: {} pts".format(score_houses(board)))
    print(board_str(board))

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
        print_status(board, score)

print_status(max_board, max_score)
