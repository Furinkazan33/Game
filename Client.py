#!/usr/bin/env python3
if __name__ == "__main__":
    raise RuntimeError("Not meant to be run")

import sys
sys.path.append("./common")

import keyboard as kbd

import Util
from Player import *
from Map import *
from typing import Optional
import ast
import asyncio
import websockets
from typing import Tuple
import keyboard as kbd
import Message

class Client:
    websocket = None
    keyboard = None
    url: str = None
    credentials: dict = None
    around: Tuple = None
    token: str = None
    player: Player = None
    main_map: Map = None
    around_map: Map = None

    def __init__(self, config: dict):
        self.websocket = None
        self.keyboard = kbd
        self.keys = config['keys']
        self.url = config['url']
        self.credentials = config['credentials']
        self.around = config['around']
        self.token = None
        self.player = None
        self.main_map = None
        self.around_map = None

        for k, v in config['keys'].items():
            #print(k, v)
            self.keyboard.add_hotkey(v, self.move, args=[k])

    async def get_player(self):
        assert self.token
        response = await self.send(Message.make_get_player(self.token))
        #TODO: erreurs
        self.player = Player(response['player'])

    async def get_map(self):
        assert self.token
        response = await self.send(Message.make_get_map(self.token))

        if self.main_map:
            self.main_map.load(response['map'])
        else:
            self.main_map = Map(response['map'])

    def get_around_map(self):
        assert self.main_map
        self.around_map = self.main_map.extract_around(self.player.position, self.around)

    def move_player(self, direction: str) -> bool:
        moved = True

        match direction:
            case 'UP':
                self.player.position.y = self.main_map.mod(self.player.position.y - 1, self.main_map.y)

            case 'DOWN':
                self.player.position.y = self.main_map.mod(self.player.position.y + 1, self.main_map.y)

            case 'LEFT':
                self.player.position.x = self.main_map.mod(self.player.position.x - 1, self.main_map.x)

            case 'RIGHT':
                self.player.position.x = self.main_map.mod(self.player.position.x + 1, self.main_map.x)

            case _:
                raise RuntimeError("Impossible movement !")

        return moved


    async def send_position(self):
        assert self.token
        response = await self.send(Message.make_position(self.token, self.player.position))

    async def move(self, direction: str):
        if self.move_player(direction):
            self.get_around_map()
            await self.send_position()

    async def run(self):
        await self.connect()
        await self.auth()

        await self.get_player()
        await self.get_map()

        while True:
            event = self.keyboard.read_event()

            if event.event_type == self.keyboard.KEY_DOWN and event.name == 'esc':
                break

        self.keyboard.unhook_all()

        await client.disconnect()

    async def send(self, message: dict) -> dict:
        print("Sending message : " + str(message))
        await self.websocket.send(message)
        serv_response = await self.websocket.recv()
        return ast.literal_eval(serv_response)

    async def auth(self):
        response = await self.send(Message.make_auth(self.credentials))
        #TODO: erreurs
        self.token = response['token']

    async def disconnect(self):
        response = await self.send(Message.make_disconnect(self.token))
        #TODO: erreurs

    async def connect(self):
        self.websocket = await websockets.connect(self.url)

