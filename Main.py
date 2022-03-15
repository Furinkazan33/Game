#!/usr/bin/env python3

def run_client(config: dict):
    client = Client(config)

    asyncio.get_event_loop().run_until_complete(client.run())



if __name__ == "__main__":

    import sys
    sys.path.append("./common")

    from Client import Client
    import asyncio

    config = {
        'keys': { 'UP': 'z', 'DOWN': 's', 'LEFT': 'q', 'RIGHT': 'd' },
        'url': 'ws://localhost:8080',
        'credentials': { 'user': 'TODO', 'password': 'TODO' },
        'around': ((20, 20), (20, 20), (20, 20)),
    }

    run_client(config)


