from enum import Enum
import uuid
import Util

class ItemStatus(Enum):
    NEW = 1
    USED = 2
    DAMAGED = 3
    BROKEN = 4

class ItemType(Enum):
    ITEM = 1
    LINGE = 2
    OUTIL = 3
    MACHINE = 4

class Item:
    id = None
    name = None
    type = None
    status = None

    def __init__(self, id=None, name="", type=ItemType.ITEM, status=ItemStatus.NEW):
        self.id = id or uuid.uuid4()
        self.name = name
        self.type = type or ItemType.ITEM
        self.status = status or ItemStatus.NEW
    
    def deserialize(line, separator=";"):
        a = line.split(separator)
        return Item(a[1], a[2], Util.str_to_instance(a[3]), Util.str_to_instance(a[4]))

    def serialize(self, separator=";"):
        return str(self.__class__.__name__) + separator + str(self.id) + separator + self.name + separator + str(self.type) + separator + str(self.status)

    def __repr__(self):
        return self.serialize()
    
    def __eq__(self, other):
        return str(self.id) == str(other.id)

if __name__ == "__main__":
    i1 = Item(None, "Marteau", ItemType.OUTIL, ItemStatus.DAMAGED)
    i2 = Item(None, "Marteau")
    i3 = Item(None)
    
    for p in [i1, i2, i3]:
        print(p)
        assert(Item.deserialize(p.serialize()).serialize() == p.serialize())
        assert(Item.deserialize(p.serialize()) == p)
