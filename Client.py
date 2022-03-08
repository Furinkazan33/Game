#!/usr/bin/env python3
import keyboard as kbd

import Util
from Item import *
from Task import *
from Player import *
from Map import *
from Loader import Loader
from typing import Optional
#import pydantic as pd


class Client:
    keys = None
    keyboard = kbd
    id = None
    main_map = None
    p_map = None
    x = None
    y = None
    z = None

    def __init__(self, config=None, main_map=None):
        self.id = config['player_infos']['id']
        self.keys = config['keys'] or { 'UP': 'z', 'DOWN': 's', 'LEFT': 'q', 'RIGHT': 'd' }
        self.keyboard.add_hotkey(self.keys['UP'], self.move, args=['UP'])
        self.keyboard.add_hotkey(self.keys['DOWN'], self.move, args=['DOWN'])
        self.keyboard.add_hotkey(self.keys['LEFT'], self.move, args=['LEFT'])
        self.keyboard.add_hotkey(self.keys['RIGHT'], self.move, args=['RIGHT'])
        self.main_map = main_map
        self.x = 0
        self.y = 0
        self.z = 0
        self.p_map = self.get_map()
        print(self.p_map)
        print(self.x, self.y, self.z)

    def send(self, message: dict):
        print("Sending message : " + str(message))


    def check(self, position, direction: str):
        print("check")
        # is_movement_possible


    def move(self, direction: str):
        match direction:
            case 'UP':
                self.y = self.main_map.mod(self.y - 1, self.main_map.y)

            case 'DOWN':
                self.y = self.main_map.mod(self.y + 1, self.main_map.y)

            case 'LEFT':
                self.x = self.main_map.mod(self.x - 1, self.main_map.x)

            case 'RIGHT':
                self.x = self.main_map.mod(self.x + 1, self.main_map.x)

            case _:
                raise RuntimeError("Impossible movement !")

        self.send({ 'auth': "auth TODO:", 'id': "id TODO:", 'type': 'player_update', 'data': { 'position': { 'x': self.x, 'y': self.y, 'z':
                                                                   self.z } } })
        self.p_map = self.get_map()
        print(self.p_map)


    def connect_server(self):
        self.send({ 'type': 'credentials', 'data': "TODO" })

    def disconnect_server(self):
        self.send({ 'type': 'disconnect', 'auth':  "todo", 'id': "todo", 'data': "TODO" })

    def get_map(self):
        distances = ((10, 10), (10, 10), (0, 0))
        return self. main_map.extract_around((self.x, self.y, self.z), distances)

    def main_loop(self):

        while True:

            event = self.keyboard.read_event()

            if event.event_type == self.keyboard.KEY_DOWN and event.name == 'esc':
                break

        self.keyboard.unhook_all()



if __name__ == "__main__":

    # TODO: get from server
    # Server.send({ 'type': 'versions' })
    # Server.on('versions'):
    #    check_versions()
    # Server.send({ 'type': 'init' })
    # Server.on('init')
    #     def get_files():
    #         items = ...
    items = Loader.load(Item, "./data/items.txt")
    players = Loader.load(Player, "./data/players.txt")
    tasks = Loader.load(Task, "./data/tasks.txt")

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


    # TODO: get from server if new version
    map_main = Map()
    map_main.load("./data/map4020.txt")

    config = { 
        'player_infos': { 
            'id': 1 
        }, 
        'keys': { 
            'UP': 'z', 'DOWN': 's', 'LEFT': 'q', 'RIGHT': 'd' 
        } 
    }
    
    client = Client(config=config, main_map=map_main)
    
    client.connect_server()
    client.main_loop()
    client.disconnect_server()



