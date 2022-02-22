from Item import *
from Person import *
from Task import *

class Loader:

    def load(classname, path: str, separator: str=";"):
        collection = []

        with open(path, 'r') as f:
            line  = f.readline().rstrip()

            while line:
                collection.append(classname.deserialize(line, separator))
                line  = f.readline().rstrip()        

        return collection

    def save(lst: list, path: str, separator=";"):
        with open(path, 'w') as f:
            for c in lst:
                f.write(c.serialize(separator) + "\n")
        

if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")