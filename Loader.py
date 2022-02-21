from Item import *
from Person import *
from Task import *

class Loader:

    def load(classname, path, separator=";"):
        collection = []

        with open(path, 'r') as f:
            line  = f.readline().rstrip()

            while line:
                collection.append(classname.deserialize(line, separator))
                line  = f.readline().rstrip()        

        return collection

    def save(collection, path, separator=";"):
        with open(path, 'w') as f:
            for c in collection:
                f.write(c.serialize(separator) + "\n")
        

if __name__ == "__main__":
    print("Not meant to be run")
