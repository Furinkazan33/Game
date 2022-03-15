#! /usr/bin/env python3

import Position

def make(m_type: str, m_data: dict or str, auth: dict or str = None) -> dict:
    return { 'type': m_type, 'data': m_data, 'auth': auth }

def make_position(auth: dict or str, position: Position) -> dict:
    return make('position', { 'x': position.x, 'y': position.y, 'z': position.z }, auth)

def make_auth(cred: dict) -> dict:
    return make('credentials', { 'user': cred['user'], 'password': cred['password'] })

def make_disconnect(auth: str or dict):
    return make('disconnect', None, auth)

def make_get_player(auth: dict or str):
    return make('get_player', None, auth)

def make_get_map(auth: dict or str):
    return make('get_map', None, auth)


