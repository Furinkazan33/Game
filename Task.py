#!/usr/bin/env python3
from enum import Enum
import uuid
import Util

class TaskType(Enum):
    Task = "Task"
    Nettoyer = "Nettoyer"
    Conduire = "Conduire"
    Travailler = "Travailler"
    Miner = "Miner"
    Shopping = "Shopping"

class Task:
    id = None
    cost = None
    name = None
    item = None
    player = None
    type = None
    
    def __init__(self, id :str=None, cost :str="", name :str="", item :str="", player :str="", type :TaskType=TaskType.Task):
        self.id = id or uuid.uuid4()
        self.cost = cost
        self.name = name
        self.item = item
        self.player = player
        self.type = type or TaskType.Task

    def deserialize(line :str, separator :str=";"):
        a = line.split(separator)
        return Task(a[1], a[2], a[3], a[4], a[5], Util.str_to_instance(a[6]))

    def serialize(self, separator :str=";"):
        return str(self.__class__.__name__) + separator + \
            str(self.id) + separator + \
            str(self.cost) + separator + \
            str(self.name) + separator + \
            str(self.item) + separator + \
            str(self.player) + separator + \
            str(self.type) 

    def __repr__(self):
        return self.serialize()

    def __eq__(self, other):
        return str(self.id) == str(other.id)

if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")
