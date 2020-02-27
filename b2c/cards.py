from collections import namedtuple

def name_set(*names):
    NameSet = namedtuple('NameSet', names)
    return NameSet(*names)

kinds = name_set('tavern', 'office', 'park', 'factory', 'shop', 'house')
KIND_LIST = [kinds.tavern, kinds.office, kinds.park, kinds.factory, kinds.shop, kinds.house]

taverns = name_set('music', 'drink', 'food', 'sleep')
TAVERN_LIST = [taverns.music, taverns.drink, taverns.food, taverns.sleep]
