#!/usr/bin/env python3
from enum import Enum, auto

class Evt(Enum):
    client_connect = auto(),
    client_disconnect = auto()


__subscribers = dict()


def subscribe(event_type: Evt, fn):
    if not event_type in __subscribers:
        __subscribers[event_type] = []
    __subscribers[event_type].append(fn)

def post_event(event_type: Evt, data):
    if not event_type in __subscribers:
        return
    for fn in __subscribers[event_type]:
        fn(data)
