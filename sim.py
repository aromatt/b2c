import sys
import random
from collections import namedtuple
from datetime import datetime

def name_set(*names):
    NameSet = namedtuple('NameSet', names)
    return NameSet(*names)

Card = namedtuple('Card', 'kind subtype')
Coord = namedtuple('Coord', 'rol col')
kinds = name_set('tavern', 'office', 'park', 'factory', 'shop', 'house')
KIND_LIST = [kinds.tavern, kinds.office, kinds.park, kinds.factory, kinds.shop, kinds.house]

BOARD_ROWS = 4
BOARD_COLS = 4

DELTA_UP = Coord(-1, 0)
DELTA_DOWN = Coord(1, 0)
DELTA_RIGHT = Coord(0, 1)
DELTA_LEFT = Coord(0, -1)

def number_of_kind(board, kind):
    return len([c for x in board for c in x if c.kind == kind])

def unique_subtypes(board, kind):
    return len(set(c.subtype for x in board for c in x if c.kind == kind))

def unique_kinds(board):
    return len(set(c.kind for x in board for c in x))

def neighbors(board, row, col, kind=None):
    return []

def score_taverns(board):
    return { 0: 0, 1: 1, 2: 4, 3: 10, 4: 12 }[unique_subtypes(board, kinds.tavern)]

def score_offices(board):
    return 3 * number_of_kind(board, kinds.office)

def score_parks(board):
    return 3 * number_of_kind(board, kinds.park)

def score_factories(board):
    num_offices = number_of_kind(board, kinds.factory)
    if num_offices == 0:
        return 0
    elif num_offices == 1:
        return 3
    else:
        return num_offices * 4

def score_shops(board):
    return 3 * number_of_kind(board, kinds.shop)

def score_houses(board):
    return unique_kinds(board) * number_of_kind(board, kinds.house)

def score_board(board):
    return score_taverns(board) + \
           score_offices(board) + \
           score_parks(board) + \
           score_factories(board) + \
           score_shops(board) + \
           score_houses(board)

def draw_card(board):
    kind = KIND_LIST[random.randint(0,len(KIND_LIST) - 1)]
    subtype = random.randint(0,3) if kind == kinds.tavern else 0
    return Card(kind, subtype)

def build_board():
    board = [[],[],[],[]]
    for row in range(0,4):
        for col in range(0,4):
            board[row].append(draw_card(board))
    return board

def is_next_to_kind(board, coord, kind):
    neighbors = filter(None,
            board_neighbor(board, coord, DELTA_UP),
            board_neighbor(board, coord, DELTA_DOWN),
            board_neighbor(board, coord, DELTA_RIGHT),
            board_neighbor(board, coord, DELTA_LEFT))
    return any(lambda n: n.kind == kind, neighbors)

def coord_add(coord, coord_delta):
    """Retuns coord modified by coord_delta or None if it would be off the board"""
    row = coord.row + coord_delta.row
    if row > BOARD_ROWS - 1 or row < 0:
        return None
    col = coord.col + coord_delta.col
    if col > BOARD_COLS - 1 or col < 0:
        return None
    return Coord(row, col)

def board_nieghbor(board, coord, coord_delta):
    """Returns neighbor of coord at coord_delta or None if it would be off the board"""
    n_coord = coord_add(coord, coord_delta)
    if n_coord is None:
        return None
    return board_get(board, n_coord)

def board_get(board, coord):
    """Returns card at given coordinates or None if it the coordinates are invalid"""
    if coord.row > BOARD_ROWS - 1 or row < 0 or coord.col > BOARD_COLS - 1 or col < 0:
        return None
    return board[coord.row][coord.col]

def print_board(board):
    for row in board:
        print '\t'.join(c.kind for c in row)

random.seed(datetime.now())

max_board = None
max_score = 0
for i in range(1000):
    board = build_board()
    score = score_board(board)
    if score > max_score:
        max_score = score
        max_board = board

print_board(max_board)
print max_score
