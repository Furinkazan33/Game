from enum import Enum
import uuid
import Util

class TaskType(Enum):
    Task = 1
    Nettoyer = 2
    Conduire = 3
    Travailler = 4
    Miner = 5
    Shopping = 6

class Task:
    id = None
    cost = None
    name = None
    item = None
    person = None
    type = None
    
    def __init__(self, id=None, cost="", name="", item="", person="", type=TaskType.Task):
        self.id = id or uuid.uuid4()
        self.cost = cost
        self.name = name
        self.item = item
        self.person = person
        self.type = type or TaskType.Task

    def deserialize(line, separator=";"):
        a = line.split(separator)
        return Task(a[1], a[2], a[3], a[4], a[5], Util.str_to_instance(a[6]))

    def serialize(self, separator=";"):
        return str(self.__class__.__name__) + separator + \
            str(self.id) + separator + \
            str(self.cost) + separator + \
            str(self.name) + separator + \
            str(self.item) + separator + \
            str(self.person) + separator + \
            str(self.type) 

    def __repr__(self):
        return self.serialize()

    def __eq__(self, other):
        return str(self.id) == str(other.id)

if __name__ == "__main__":
    p1 = Task(None, "2", "t1", None, None, None)
    p2 = Task(None, "1", "t2", "10", None, None)
    p3 = Task(None, "3", "t3", "7", None, None)

    for p in [p1, p2, p3]:
        print(p)
        assert(Task.deserialize(p.serialize()).serialize() == p.serialize())
        assert(Task.deserialize(p.serialize()) == p)
