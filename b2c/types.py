from collections import namedtuple

def name_set(*names):
    NameSet = namedtuple('NameSet', names)
    return NameSet(*names)

Building = namedtuple('Building', 'kind subtype')
PlacedBuilding = namedtuple('PlacedBuilding', 'building coord is_duplex')
Duplex = namedtuple('Duplex', 'a b delta')

kinds = name_set('tavern', 'office', 'park', 'factory', 'shop', 'house')
KIND_LIST = [kinds.tavern, kinds.office, kinds.park, kinds.factory, kinds.shop, kinds.house]

taverns = name_set('music', 'drink', 'food', 'sleep')
TAVERN_LIST = [taverns.music, taverns.drink, taverns.food, taverns.sleep]

Coord = namedtuple('Coord', 'row col')
DELTA_UP = Coord(-1, 0)
DELTA_DOWN = Coord(1, 0)
DELTA_RIGHT = Coord(0, 1)
DELTA_LEFT = Coord(0, -1)
ADJACENT_DELTAS = [DELTA_UP, DELTA_DOWN, DELTA_RIGHT, DELTA_LEFT]
