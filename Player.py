#!/usr/bin/env python3
from enum import Enum
import uuid
import Util

class Player:
    id = None
    lastname = None
    name = None
    age = None
    
    def __init__(self, id: str, lastname: str="", name: str="", age: str=""):
        self.id = id or str(uuid.uuid4())
        self.lastname = lastname
        self.name = name
        self.age = age

    def deserialize(line: str, separator: str=";"):
        a = line.split(separator)
        return Player(a[1], a[2], a[3], a[4])

    def serialize(self, separator: str=";"):
        return str(self.__class__.__name__) + separator + str(self.id) + separator + self.lastname + separator + self.name + separator + str(self.age)

    def __repr__(self):
        return self.serialize()

    def __eq__(self, other):
        return str(self.id) == str(other.id)

if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")


