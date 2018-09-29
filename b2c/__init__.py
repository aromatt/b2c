from __future__ import print_function
import random
import copy
from collections import namedtuple

def name_set(*names):
    NameSet = namedtuple('NameSet', names)
    return NameSet(*names)

Card = namedtuple('Card', 'kind subtype')
PlacedCard = namedtuple('PlacedCard', 'card coord')
Coord = namedtuple('Coord', 'row col')
kinds = name_set('tavern', 'office', 'park', 'factory', 'shop', 'house')
taverns = name_set('music', 'drink', 'food', 'sleep')
ROWS = 4
COLS = 4

DELTA_UP = Coord(-1, 0)
DELTA_DOWN = Coord(1, 0)
DELTA_RIGHT = Coord(0, 1)
DELTA_LEFT = Coord(0, -1)
ADJACENT_DELTAS = [DELTA_UP, DELTA_DOWN, DELTA_RIGHT, DELTA_LEFT]

KIND_LIST = [kinds.tavern, kinds.office, kinds.park, kinds.factory, kinds.shop, kinds.house]
TAVERN_LIST = [
    taverns.music,
    taverns.drink,
    taverns.food,
    taverns.sleep
]

TAVERN_SCORING = [1, 4, 9, 17]
OFFICE_SCORING = [1, 3, 6, 10, 15, 21]
SHOP_SCORING = [2, 5, 10, 16]
PARK_SCORING = [2, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def get_each(board, kind):
    return [pc for row in board for pc in row if pc and pc.card.kind == kind]

def number_of_kind(board, kind):
    return len(get_each(board, kind))

def num_unique_subtypes(board, kind):
    return len(set(pc.card.subtype for row in board
                   for pc in row if pc and pc.card.kind == kind))

def num_unique_kinds(board):
    return len(set(pc.card.kind for row in board for pc in row if pc))

def neighbors(board, coord, kind=None):
    """Returns PlacedCards"""
    ns = []
    for delta in ADJACENT_DELTAS:
        ncoord = coord_add(coord, delta)
        if ncoord is None:
            continue
        n = board_get(board, ncoord)
        if n is None:
            continue
        if kind is None or n.card.kind == kind:
            ns.append(n)
    return ns

def draw_card(board):
    kind = KIND_LIST[random.randint(0,len(KIND_LIST) - 1)]
    if kind == kinds.tavern:
        subtype = random.choice(TAVERN_LIST)
    else:
        subtype = None
    return Card(kind, subtype)

def place_card(board, coord, card):
    pc = PlacedCard(card, coord)
    board[coord.row][coord.col] = pc

def empty_board():
    board = []
    for row in range(ROWS):
        board.append([])
        for col in range(COLS):
            board[row].append(None)
    return board

def build_board():
    board = empty_board()
    for row in range(0, ROWS):
        for col in range(0, COLS):
            place_card(board, Coord(row, col), draw_card(board))
    return board

def is_next_to_kind(board, coord, kind):
    for delta in ADJACENT_DELTAS:
        n = board_neighbor(board, coord, delta)
        if n and n.card.kind == kind:
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
    """Returns card at given coordinates or None if it the coordinates are invalid"""
    if coord.row > ROWS - 1 or coord.row < 0 or coord.col > COLS - 1 or coord.col < 0:
        return None
    return board[coord.row][coord.col]

def card_str(card):
    if card.kind == kinds.tavern:
        return 't({})'.format(card.subtype)
    else:
        return card.kind

def board_str(board):
    return ''.join('\n' + '    \t'.join(card_str(pc.card) if pc else '    ' for pc in row)
                   for row in board)

def score_taverns(board):
    sets = []
    for pc in get_each(board, kinds.tavern):
        chosen_set = next((s for s in sets if pc.card.subtype not in s), None)
        if chosen_set is None:
            chosen_set = set()
            sets.append(chosen_set)
        chosen_set.add(pc.card.subtype)
    score = sum(TAVERN_SCORING[len(s) - 1] for s in sets)
    return score

def score_offices(board):
    total = 0
    count = 0
    for pc in get_each(board, kinds.office):
        if count < len(TAVERN_SCORING) - 1:
            total += TAVERN_SCORING[count]
            count += 1
        else:
            total += 1
        if is_next_to_kind(board, pc.coord, kinds.tavern):
            total += 1
    return total

def score_factories(board, threshold=3):
    """Assume we have the most factories if we have > `threshold` factories, and that we
    have the least if we have 0."""
    num_factories = number_of_kind(board, kinds.factory)
    if num_factories == 0:
        return 0
    elif num_factories == threshold:
        return 3
    else:
        return num_factories * 4

def score_houses(board):
    num_uniques = num_unique_kinds(board)
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
