#!/usr/bin/env python2

from __future__ import print_function
from b2c import *

def assert_score(expected, actual):
    assert expected == actual, "Expected {}, got {}".format(expected, actual)

def test_taverns():
    print('taverns... ', end='')

    board = empty_board()
    place_card(board, Coord(0,0), Card(kinds.tavern, taverns.food))
    place_card(board, Coord(1,0), Card(kinds.tavern, taverns.drink))
    place_card(board, Coord(2,0), Card(kinds.tavern, taverns.sleep))
    place_card(board, Coord(3,0), Card(kinds.tavern, taverns.music))
    assert_score(17, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,0), Card(kinds.tavern, taverns.food))
    place_card(board, Coord(1,0), Card(kinds.tavern, taverns.drink))
    place_card(board, Coord(2,0), Card(kinds.tavern, taverns.sleep))
    place_card(board, Coord(3,0), Card(kinds.tavern, taverns.music))
    place_card(board, Coord(0,1), Card(kinds.tavern, taverns.food))
    place_card(board, Coord(1,1), Card(kinds.tavern, taverns.drink))
    assert_score(21, score_board(board))

    print('OK')

def test_shops():
    print('shops... ', end='')

    board = empty_board()
    place_card(board, Coord(0,1), Card(kinds.shop, None))
    assert_score(2, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,1), Card(kinds.shop, None))
    place_card(board, Coord(1,1), Card(kinds.shop, None))
    place_card(board, Coord(2,1), Card(kinds.shop, None))
    assert_score(10, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,1), Card(kinds.shop, None))
    place_card(board, Coord(1,1), Card(kinds.shop, None))
    place_card(board, Coord(2,1), Card(kinds.shop, None))
    place_card(board, Coord(0,2), Card(kinds.shop, None))
    place_card(board, Coord(1,2), Card(kinds.shop, None))
    place_card(board, Coord(2,2), Card(kinds.shop, None))
    assert_score(20, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,1), Card(kinds.shop, None))
    place_card(board, Coord(1,1), Card(kinds.shop, None))
    place_card(board, Coord(2,1), Card(kinds.shop, None))
    place_card(board, Coord(0,3), Card(kinds.shop, None))
    place_card(board, Coord(1,3), Card(kinds.shop, None))
    place_card(board, Coord(2,3), Card(kinds.shop, None))
    assert_score(20, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,0), Card(kinds.shop, None))
    place_card(board, Coord(1,0), Card(kinds.shop, None))
    place_card(board, Coord(2,0), Card(kinds.shop, None))
    place_card(board, Coord(0,1), Card(kinds.shop, None))
    place_card(board, Coord(0,2), Card(kinds.shop, None))
    assert_score(15, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,1), Card(kinds.shop, None))
    place_card(board, Coord(1,1), Card(kinds.shop, None))
    place_card(board, Coord(2,1), Card(kinds.shop, None))
    place_card(board, Coord(3,1), Card(kinds.shop, None))
    place_card(board, Coord(2,0), Card(kinds.shop, None))
    place_card(board, Coord(2,2), Card(kinds.shop, None))
    place_card(board, Coord(2,3), Card(kinds.shop, None))
    assert_score(23, score_board(board))

    print("OK")

def test_parks():
    print('parks... ', end='')

    board = empty_board()
    place_card(board, Coord(0,0), Card(kinds.park, None))
    assert_score(2, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,0), Card(kinds.park, None))
    place_card(board, Coord(1,0), Card(kinds.park, None))
    assert_score(8, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,0), Card(kinds.park, None))
    place_card(board, Coord(1,0), Card(kinds.park, None))
    place_card(board, Coord(0,1), Card(kinds.park, None))
    assert_score(12, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,0), Card(kinds.park, None))
    place_card(board, Coord(1,0), Card(kinds.park, None))
    place_card(board, Coord(0,1), Card(kinds.park, None))
    place_card(board, Coord(1,1), Card(kinds.park, None))
    assert_score(13, score_board(board))

    board = empty_board()
    place_card(board, Coord(0,0), Card(kinds.park, None))
    place_card(board, Coord(1,0), Card(kinds.park, None))
    place_card(board, Coord(0,2), Card(kinds.park, None))
    place_card(board, Coord(1,2), Card(kinds.park, None))
    assert_score(16, score_board(board))

    print("OK")


test_parks()
test_taverns()
test_shops()
