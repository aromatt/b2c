from collections import namedtuple

Building = namedtuple('Building', 'kind subtype')
PlacedBuilding = namedtuple('PlacedBuilding', 'building coord is_duplex')
Duplex = namedtuple('Duplex', 'a b delta')

Coord = namedtuple('Coord', 'row col')
DELTA_UP = Coord(-1, 0)
DELTA_DOWN = Coord(1, 0)
DELTA_RIGHT = Coord(0, 1)
DELTA_LEFT = Coord(0, -1)
ADJACENT_DELTAS = [DELTA_UP, DELTA_DOWN, DELTA_RIGHT, DELTA_LEFT]
