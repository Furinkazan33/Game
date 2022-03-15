#!/usr/bin/env python3
if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")

from enum import Enum
import uuid
import Util
import Position

class Player:
    id: str
    pseudo: str
    config: dict
    position: Position

    def __init__(self, id: str, pseudo: str, config: dict, position: Position):
        self.id = id
        self.pseudo = pseudo
        self.config = config
        self.position = position

    def deserialize(line: str, separator: str=";"):
        a = line.split(separator)
        return Player(a[1], a[2], a[3], a[4])

    def serialize(self, separator: str=";"):
        return str(self.__class__.__name__) + separator + str(self.id) + separator + self.lastname + separator + self.name + separator + str(self.age)

    def __repr__(self):
        return self.serialize()

    def __eq__(self, other):
        return str(self.id) == str(other.id)


