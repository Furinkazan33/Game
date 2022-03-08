#!/usr/bin/env python3
if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")

class Position:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

    
