#!/usr/bin/env python

from __future__ import print_function
from datetime import datetime
import random
import sys
from b2c import *

def print_status(board, score):
    print(f'\nbest board ({score}):')
    print(f'  shops: {score_shops(board)} pts')
    print(f'  factories: {score_factories(board)} pts')
    print(f'  taverns: {score_taverns(board)} pts')
    print(f'  offices: {score_offices(board)} pts')
    print(f'  parks: {score_parks(board)} pts')
    print(f'  houses: {score_houses(board)} pts')
    print(board_str(board))

if len(sys.argv) > 1:
    iterations = int(sys.argv[1])
else:
    iterations = 10000

print(f'Trying {iterations} boards')
random.seed(datetime.now())
max_board = None
max_score = 0
tried_boards = set()
for i in range(iterations):
    if i % 5000 == 0:
        print(f'boards done: {i}; max score: {max_score}')
        sys.stdout.flush()
    board = build_board()
    score = score_board(board)
    if score > max_score:
        max_score = score
        max_board = board
        print_status(board, score)

print_status(max_board, max_score)
