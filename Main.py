#!/usr/bin/env python3
import Util
from Item import *
from Task import *
from Player import *
from Map import *
from Loader import Loader
from event import *


def print_menu():
    print("Menu")


def find_by_id(lst: str, id: str):
    try:
        return next(c for c in lst if c.id == id)

    except StopIteration:
        raise LookupError(str(id) + " not found !")


if __name__ == "__main__":


    # Test des chargements de fichiers data
    items = Loader.load(Item, "./data/items.txt")
    players = Loader.load(Player, "./data/players.txt")
    tasks = Loader.load(Task, "./data/tasks.txt")
    

    # Test de la sérialisation
    for item in items:
        print(item)
        assert(Item.deserialize(item.serialize()).serialize() == item.serialize())
        assert(Item.deserialize(item.serialize()) == item)

    for player in players:
        print(player)
        assert(Player.deserialize(player.serialize()).serialize() == player.serialize())
        assert(Player.deserialize(player.serialize()) == player)

    for task in tasks:
        print(task)
        assert(Task.deserialize(task.serialize()).serialize() == task.serialize())
        assert(Task.deserialize(task.serialize()) == task)

    for i in tasks:
        if i.player:
            p = find_by_id(players, i.player)

            if p:
                print("In task : " + i.__repr__() + " player found : " + p.__repr__())


    # Test des map
    map_main = Map()
    map_main.load("./data/map4020.txt")
    print(map_main)
    map_main.save("./data/_bak_map4020.txt")
    
    position = (0, 0, 0)
    distances = ((10, 10), (10, 10), (0, 0))
    map_extracted = map_main.extract_around(position, distances)
    print(map_extracted)


    # Test des event/observer
    def test(data):
        print(data)

    subscribe(Evt.client_connect, test)
    post_event(Evt.client_connect, "un test")



