import random
from collections import namedtuple
from b2c.types import *

class Box(object):

    # Cards in a box https://boardgamegeek.com/image/2439667/pard
    def __init__(self):
        self.buildings = self._init_buildings()
        self.duplexes = self._init_duplexes()

    def _init_buildings(self):
        buildings = []
        for kind in [kinds.shop, kinds.factory, kinds.park]:
            for i in range(16):
                buildings.append(Building(kind, None))
        for kind in [kinds.office, kinds.house]:
            for i in range(16):
                buildings.append(Building(kind, None))
        for subtype in TAVERN_LIST:
            for i in range(5):
                buildings.append(Building(kind, subtype))
        return buildings

    def _init_duplexes(self):
        return [
            Duplex(Building(kinds.factory, None), Building(kinds.shop, None), DELTA_RIGHT),
            Duplex(Building(kinds.shop, None), Building(kinds.tavern, taverns.music), DELTA_RIGHT),
            Duplex(Building(kinds.office, None), Building(kinds.shop, None), DELTA_RIGHT),
            Duplex(Building(kinds.shop, None), Building(kinds.house, None), DELTA_RIGHT),
            Duplex(Building(kinds.shop, None), Building(kinds.factory, None), DELTA_DOWN),
            Duplex(Building(kinds.tavern, taverns.food), Building(kinds.factory, None), DELTA_RIGHT),
            Duplex(Building(kinds.factory, None), Building(kinds.office, None), DELTA_RIGHT),
            Duplex(Building(kinds.park, None), Building(kinds.factory, None), DELTA_RIGHT),
            Duplex(Building(kinds.factory, None), Building(kinds.tavern, taverns.food), DELTA_DOWN),
            Duplex(Building(kinds.tavern, taverns.drink), Building(kinds.park, None), DELTA_RIGHT),
            Duplex(Building(kinds.shop, None), Building(kinds.tavern, taverns.sleep), DELTA_DOWN),
            Duplex(Building(kinds.house, None), Building(kinds.tavern, taverns.sleep), DELTA_RIGHT),
            Duplex(Building(kinds.office, None), Building(kinds.shop, None), DELTA_DOWN),
            Duplex(Building(kinds.factory, None), Building(kinds.office, None), DELTA_DOWN),
            Duplex(Building(kinds.park, None), Building(kinds.office, None), DELTA_RIGHT),
            Duplex(Building(kinds.office, None), Building(kinds.house, None), DELTA_RIGHT),
            Duplex(Building(kinds.park, None), Building(kinds.factory, None), DELTA_DOWN),
            Duplex(Building(kinds.tavern, taverns.music), Building(kinds.park, None), DELTA_DOWN),
            Duplex(Building(kinds.office, None), Building(kinds.park, None), DELTA_DOWN),
            Duplex(Building(kinds.house, None), Building(kinds.park, None), DELTA_RIGHT),
            Duplex(Building(kinds.house, None), Building(kinds.shop, None), DELTA_DOWN),
            Duplex(Building(kinds.tavern, taverns.drink), Building(kinds.house, None), DELTA_DOWN),
            Duplex(Building(kinds.house, None), Building(kinds.office, None), DELTA_DOWN),
            Duplex(Building(kinds.park, None), Building(kinds.house, None), DELTA_DOWN)]

    def draw_building(self):
        i = random.randint(0, len(self.buildings) - 1)
        return self.buildings.pop(i)

    def draw_duplex(self):
        """Returned as two buildings and a Coord to represent their relative positioning"""
        i = random.randint(0, len(self.duplexes) - 1)
        return self.duplexes.pop(i)
