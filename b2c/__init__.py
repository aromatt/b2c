from __future__ import print_function
import random
import copy
from collections import namedtuple
from b2c.box import Box
from b2c.types import *
from b2c.cards import kinds, taverns

ROWS = 4
COLS = 4

TAVERN_SCORING = [1, 4, 9, 17]
OFFICE_SCORING = [1, 2, 3, 4, 5, 6] # deltas
SHOP_SCORING = [2, 5, 10, 16]
PARK_SCORING = [2, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def get_each(board, kind):
    return [pb for row in board for pb in row if pb and pb.building.kind == kind]

def number_of_kind(board, kind):
    return len(get_each(board, kind))

def num_unique_subtypes(board, kind):
    return len(set(pb.building.subtype for row in board
                   for pb in row if pb and pb.building.kind == kind))

def num_unique_kinds(board):
    return len(set(pb.building.kind for row in board for pb in row if pb))

def neighbors(board, coord, kind=None):
    """Returns PlacedBuildings"""
    ns = []
    for delta in ADJACENT_DELTAS:
        ncoord = coord_add(coord, delta)
        if ncoord is None:
            continue
        n = board_get(board, ncoord)
        if n is None:
            continue
        if kind is None or n.building.kind == kind:
            ns.append(n)
    return ns

def place_building(board, coord, building, is_duplex=False):
    if board[coord.row][coord.col] is not None:
        raise Exception("Tried to place a building on an occupied space")
    pb = PlacedBuilding(building, coord, is_duplex)
    board[coord.row][coord.col] = pb

def empty_board():
    board = []
    for row in range(ROWS):
        board.append([])
        for col in range(COLS):
            board[row].append(None)
    return board

def duplex_neighbor_available(coord, duplex):
    n_coord = coord_add(coord, duplex)
    if n_coord and board[coord.row][coord.col] is None:
        return True
    return False

def get_empty_spaces(board):
    spaces = []
    for row in range(0, ROWS):
        for col in range(0, COLS):
            coord = Coord(row, col)
            if board_get(board, coord) is None:
                spaces.append(coord)
    return spaces

def play_building_round(board, box, num_cards):
    empty_spaces = get_empty_spaces(board)
    for i in range(0, num_cards):
        building = box.draw_building()
        coord = random.choice(empty_spaces)
        empty_spaces.remove(coord)
        place_building(board, coord, building)

def play_duplex_round(board, box, num_cards):
    empty_spaces = get_empty_spaces(board)
    for i in range(0, num_cards):
        duplex = box.draw_duplex()
        while True:
            a_coord = random.choice(empty_spaces)
            b_coord = coord_add(a_coord, duplex.delta)
            if b_coord in empty_spaces:
                break
        empty_spaces.remove(a_coord)
        empty_spaces.remove(b_coord)
        place_building(board, a_coord, duplex.a, True)
        place_building(board, b_coord, duplex.b, True)

def build_board():
    board = empty_board()
    box = Box()
    play_duplex_round(board, box, 2)
    play_building_round(board, box, 6)
    play_building_round(board, box, 6)
    return board

def is_next_to_kind(board, coord, kind):
    for delta in ADJACENT_DELTAS:
        n = board_neighbor(board, coord, delta)
        if n and n.building.kind == kind:
            return True
    return False

def coord_add(coord, coord_delta):
    """Retuns coord modified by coord_delta or None if it would be off the board"""
    row = coord.row + coord_delta.row
    if row > ROWS - 1 or row < 0:
        return None
    col = coord.col + coord_delta.col
    if col > COLS - 1 or col < 0:
        return None
    return Coord(row, col)

def board_neighbor(board, coord, coord_delta):
    """Returns neighbor of coord at coord_delta or None if it would be off the board"""
    n_coord = coord_add(coord, coord_delta)
    if n_coord is None:
        return None
    return board_get(board, n_coord)

def board_get(board, coord):
    """Returns building at given coordinates or None if it the coordinates are invalid"""
    if coord.row > ROWS - 1 or coord.row < 0 or coord.col > COLS - 1 or coord.col < 0:
        return None
    return board[coord.row][coord.col]

def placed_building_str(pb):
    if pb is None:
        return '    '
    if pb.building.kind == kinds.tavern:
        string = f't({pb.building.subtype})'
    else:
        string =  pb.building.kind
    if pb.is_duplex:
        string += '*'
    return string

def board_str(board):
    string = '\n'
    for row in board:
        for pb in row:
            string += placed_building_str(pb) + '    \t'
        string += '\n'
    return string

def score_taverns(board):
    sets = []
    for pb in get_each(board, kinds.tavern):
        chosen_set = next((s for s in sets if pb.building.subtype not in s), None)
        if chosen_set is None:
            chosen_set = set()
            sets.append(chosen_set)
        chosen_set.add(pb.building.subtype)
    score = sum(TAVERN_SCORING[len(s) - 1] for s in sets)
    return score

def score_offices(board):
    total = 0
    for i, pb in enumerate(get_each(board, kinds.office)):
        total += OFFICE_SCORING[i % len(OFFICE_SCORING)]
        if is_next_to_kind(board, pb.coord, kinds.tavern):
            total += 1
    return total

def score_factories(board, threshold=3):
    """Assume we have the most factories if we have > `threshold` factories, and that we
    have the least if we have 0."""
    num_factories = number_of_kind(board, kinds.factory)
    if num_factories == 0:
        return 0
    elif num_factories == threshold:
        return num_factories * 2
    else:
        return num_factories * 4

def score_houses(board):
    num_uniques = num_unique_kinds(board) - 1 # minus 1 bc houses don't count
    total = 0
    for h in get_each(board, kinds.house):
        if not is_next_to_kind(board, h.coord, kinds.factory):
            total += num_uniques
        else:
            total += 1
    return total

def score_shops(board):
    """Approach: Find longest line of shops on board, then remove it. Repeat until
    all shops are gone."""
    def longest_line_including(shop, shops):
        """Only searches in increasing coords; assumes shops are sorted"""
        longest = []
        for delta in [DELTA_DOWN, DELTA_RIGHT]:
            cur_line = []
            coord = shop.coord
            while any(coord == s.coord for s in shops): # is a shop
                cur_line.append(coord)
                coord = coord_add(coord, delta)
                if coord is None:
                    break
            if len(cur_line) > len(longest):
                longest = cur_line
        return longest
    shops = sorted(copy.deepcopy(get_each(board, kinds.shop)))
    score = 0
    while len(shops) > 0:
        longest = []
        for s in shops:
            s_longest = longest_line_including(s, shops)
            if len(s_longest) > len(longest):
                longest = s_longest
        score += SHOP_SCORING[len(longest) - 1]
        for member in longest:
            shops = [s for s in shops if not s.coord == member]
    return score

def score_parks(board):
    parks = sorted(copy.deepcopy(get_each(board, kinds.park)))
    score = 0
    def build_cluster(p, cluster=set([])):
        cluster |= set([p.coord])
        for n in neighbors(board, p.coord, kind=kinds.park):
            if n.coord in cluster:
                continue
            cluster |= build_cluster(n, cluster)
        return cluster
    while len(parks) > 0:
        cluster = build_cluster(parks[0], set([]))
        score += PARK_SCORING[len(cluster) - 1]
        for member in cluster:
            parks = [p for p in parks if not p.coord == member]
    return score

def score_board(board):
    return score_taverns(board) + \
           score_offices(board) + \
           score_parks(board) + \
           score_factories(board) + \
           score_shops(board) + \
           score_houses(board)
