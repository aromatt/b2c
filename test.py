#!/usr/bin/env python

from __future__ import print_function
from b2c import *

def assert_score(expected, actual):
    assert expected == actual, f'Expected {expected}, got {actual}'

def test_offices():
    print('offices... ', end='')

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.office, None))
    assert_score(1, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.office, None))
    place_building(board, Coord(1,0), Building(kinds.office, None))
    place_building(board, Coord(2,0), Building(kinds.office, None))
    place_building(board, Coord(3,0), Building(kinds.office, None))
    place_building(board, Coord(0,1), Building(kinds.office, None))
    place_building(board, Coord(1,1), Building(kinds.office, None))
    assert_score(21, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.office, None))
    place_building(board, Coord(1,0), Building(kinds.office, None))
    place_building(board, Coord(2,0), Building(kinds.office, None))
    place_building(board, Coord(3,0), Building(kinds.office, None))
    place_building(board, Coord(0,1), Building(kinds.office, None))
    place_building(board, Coord(1,1), Building(kinds.office, None))
    place_building(board, Coord(2,1), Building(kinds.office, None))
    assert_score(22, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.office, None))
    place_building(board, Coord(1,0), Building(kinds.office, None))
    place_building(board, Coord(2,0), Building(kinds.office, None))
    place_building(board, Coord(3,0), Building(kinds.office, None))
    place_building(board, Coord(0,1), Building(kinds.office, None))
    place_building(board, Coord(1,1), Building(kinds.office, None))
    place_building(board, Coord(2,1), Building(kinds.office, None))
    place_building(board, Coord(3,1), Building(kinds.office, None))
    place_building(board, Coord(0,2), Building(kinds.office, None))
    place_building(board, Coord(1,2), Building(kinds.office, None))
    place_building(board, Coord(2,2), Building(kinds.office, None))
    place_building(board, Coord(3,2), Building(kinds.office, None))
    assert_score(42, score_board(board))

    print('OK')


def test_taverns():
    print('taverns... ', end='')

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.tavern, taverns.food))
    place_building(board, Coord(1,0), Building(kinds.tavern, taverns.drink))
    place_building(board, Coord(2,0), Building(kinds.tavern, taverns.sleep))
    place_building(board, Coord(3,0), Building(kinds.tavern, taverns.music))
    assert_score(17, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.tavern, taverns.food))
    place_building(board, Coord(1,0), Building(kinds.tavern, taverns.drink))
    place_building(board, Coord(2,0), Building(kinds.tavern, taverns.sleep))
    place_building(board, Coord(3,0), Building(kinds.tavern, taverns.music))
    place_building(board, Coord(0,1), Building(kinds.tavern, taverns.food))
    place_building(board, Coord(1,1), Building(kinds.tavern, taverns.drink))
    assert_score(21, score_board(board))

    print('OK')

def test_shops():
    print('shops... ', end='')

    board = empty_board()
    place_building(board, Coord(0,1), Building(kinds.shop, None))
    assert_score(2, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,1), Building(kinds.shop, None))
    place_building(board, Coord(1,1), Building(kinds.shop, None))
    place_building(board, Coord(2,1), Building(kinds.shop, None))
    assert_score(10, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,1), Building(kinds.shop, None))
    place_building(board, Coord(1,1), Building(kinds.shop, None))
    place_building(board, Coord(2,1), Building(kinds.shop, None))
    place_building(board, Coord(0,2), Building(kinds.shop, None))
    place_building(board, Coord(1,2), Building(kinds.shop, None))
    place_building(board, Coord(2,2), Building(kinds.shop, None))
    assert_score(20, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,1), Building(kinds.shop, None))
    place_building(board, Coord(1,1), Building(kinds.shop, None))
    place_building(board, Coord(2,1), Building(kinds.shop, None))
    place_building(board, Coord(0,3), Building(kinds.shop, None))
    place_building(board, Coord(1,3), Building(kinds.shop, None))
    place_building(board, Coord(2,3), Building(kinds.shop, None))
    assert_score(20, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.shop, None))
    place_building(board, Coord(1,0), Building(kinds.shop, None))
    place_building(board, Coord(2,0), Building(kinds.shop, None))
    place_building(board, Coord(0,1), Building(kinds.shop, None))
    place_building(board, Coord(0,2), Building(kinds.shop, None))
    assert_score(15, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,1), Building(kinds.shop, None))
    place_building(board, Coord(1,1), Building(kinds.shop, None))
    place_building(board, Coord(2,1), Building(kinds.shop, None))
    place_building(board, Coord(3,1), Building(kinds.shop, None))
    place_building(board, Coord(2,0), Building(kinds.shop, None))
    place_building(board, Coord(2,2), Building(kinds.shop, None))
    place_building(board, Coord(2,3), Building(kinds.shop, None))
    assert_score(23, score_board(board))

    print("OK")

def test_parks():
    print('parks... ', end='')

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.park, None))
    assert_score(2, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.park, None))
    place_building(board, Coord(1,0), Building(kinds.park, None))
    assert_score(8, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.park, None))
    place_building(board, Coord(1,0), Building(kinds.park, None))
    place_building(board, Coord(0,1), Building(kinds.park, None))
    assert_score(12, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.park, None))
    place_building(board, Coord(1,0), Building(kinds.park, None))
    place_building(board, Coord(0,1), Building(kinds.park, None))
    place_building(board, Coord(1,1), Building(kinds.park, None))
    assert_score(13, score_board(board))

    board = empty_board()
    place_building(board, Coord(0,0), Building(kinds.park, None))
    place_building(board, Coord(1,0), Building(kinds.park, None))
    place_building(board, Coord(0,2), Building(kinds.park, None))
    place_building(board, Coord(1,2), Building(kinds.park, None))
    assert_score(16, score_board(board))

    print("OK")


test_offices()
test_parks()
test_taverns()
test_shops()
