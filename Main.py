import Util
from Item import *
from Task import *
from Person import *
from Map import *
from Loader import Loader



def print_menu():
    print("Menu")


def find_by_id(collection, id):
    try:
        return next(c for c in collection if c.id == id)

    except StopIteration:
        raise LookupError(str(id) + " not found !")


if __name__ == "__main__":

    items = Loader.load(Item, "./data/items.txt")
    persons = Loader.load(Person, "./data/persons.txt")
    tasks = Loader.load(Task, "./data/tasks.txt")
    map_main = Map()
    map_main.load("./data/map4020.txt")
    print(map_main)
    
    position = (0, 0, 0)
    distances = ((10, 10), (10, 10), (0, 0))
    map_extracted = map_main.extract_around(position, distances)
    print(map_extracted)

    for i in tasks:
        if i.person:
            p = find_by_id(persons, i.person)

            if p:
                print("In task : " + i.__repr__() + " person found : " + p.__repr__())



