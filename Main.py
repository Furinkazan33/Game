import Util
from Item import *
from Task import *
from Person import *
from Map import *
from Loader import Loader



def print_menu():
    print("Menu")


def find_by_id(lst: str, id: str):
    try:
        return next(c for c in lst if c.id == id)

    except StopIteration:
        raise LookupError(str(id) + " not found !")


if __name__ == "__main__":

    items = Loader.load(Item, "./data/items.txt")
    persons = Loader.load(Person, "./data/persons.txt")
    tasks = Loader.load(Task, "./data/tasks.txt")

    for item in items:
        print(item)
        assert(Item.deserialize(item.serialize()).serialize() == item.serialize())
        assert(Item.deserialize(item.serialize()) == item)

    for person in persons:
        print(person)
        assert(Person.deserialize(person.serialize()).serialize() == person.serialize())
        assert(Person.deserialize(person.serialize()) == person)

    for task in tasks:
        print(task)
        assert(Task.deserialize(task.serialize()).serialize() == task.serialize())
        assert(Task.deserialize(task.serialize()) == task)

    for i in tasks:
        if i.person:
            p = find_by_id(persons, i.person)

            if p:
                print("In task : " + i.__repr__() + " person found : " + p.__repr__())

    map_main = Map()
    map_main.load("./data/map4020.txt")
    print(map_main)
    map_main.save("./data/_bak_map4020.txt")
    
    position = (0, 0, 0)
    distances = ((10, 10), (10, 10), (0, 0))
    map_extracted = map_main.extract_around(position, distances)
    print(map_extracted)

    a = [(1, 2), (3,4 ), (5, 6)]
    b, c, d = a
    print(b)