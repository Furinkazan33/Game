from enum import Enum
from os import X_OK
from typing import Mapping, Tuple
import uuid
import Util

class BlocType(Enum):
    EMPTY = ' '
    DIRT = 'b'
    SAND = 'c'
    WATER = 'd'
    ROCK = 'e'
    WALL = 'f'


"""
    3D Circular Map
"""
class Map:
    id = None
    x = None
    y = None
    z = None
    blocs = None
    
    def __init__(self, id: str=None, blocs: list=None, x: int=None, y: int=None, z: int=None, path:str =None):
        self.id = id or str(uuid.uuid4())
        self.blocs = blocs or []
        self.x = x
        self.y = y
        self.z = z
    
    a = []
    a.append([])
    a[0].append([])


    def load(self, path: str):
        with open(path, 'r') as f:
            line = f.readline()
            line = line.rstrip()
            (self.x, self.y, self.z) = tuple(map(int, line.split(' ')))

            
            for z in range(0, self.z):
                self.blocs.append([])

                for y in range(0, self.y):
                    line = f.readline()
                    line = line.rstrip()
                    line = line[:-1]
                    new_line = []
                
                    for c in line:
                        new_line.append(BlocType(c))
                
                    self.blocs[z].append(new_line)
    


    def save(self, path: str):
        with open(path, 'w') as f:
            f.write(self.__repr__())

    """
    Returns the modulo value of the given value according to the max
    """
    def __mod(self, value: int, max: int):
        if value < 0:
            return max + value
		
        if value >= max:
            return value - max + 1
		
        return value
	
    """
    Creates a new Map from extracting the current map around the given position (x, y, z)
    and the given distances ((dx_before, dx_after), (dy_before, dy_after), (dz_before, dz_after))
    """
    def extract_around(self, position: Tuple, distance: Tuple):
        # Coordinates
        (px, py, pz) = position
        # distance before and after position
        ((dx_before, dx_after), (dy_before, dy_after), (dz_before, dz_after)) = distance

        map_extracted = []

        for z in range(pz - dz_before, pz + dz_after + 1):
            map_extracted.append([])

            for y in range(py - dy_before, py + dy_after + 1):
                map_extracted[z - (pz - dz_before)].append([])

                for x in range(px - dx_before, px + dx_after + 1):
                    iz = self.__mod(z, self.z)
                    iy = self.__mod(y, self.y)
                    ix = self.__mod(x, self.x)
                    map_extracted[z - (pz - dz_before)][y - (py - dy_before)].append(self.blocs[iz][iy][ix])

        return Map(None, map_extracted, dx_before + dx_after + 1, dy_before + dy_after + 1, dz_before + dz_after + 1)

    """
    2D representation of the map
    """
    def __repr__(self):
        res = str(self.x) + " " + str(self.y) + " " + str(self.z) + "\n"

        for z in self.blocs:
            for y in z:
                for x in y:
                    res += x.value
                res += ";\n"

        return res

    def __eq__(self, other):
        return str(self.id) == str(other.id)
        



if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")
    


    

    