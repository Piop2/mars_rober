from utils.json_data import encode, decode
from utils.image import decode_image


def send(client, data):
    msg = encode(data)
    client.send(msg)
    return


def receive(client):
    msg = client.recv(1024)
    if not msg:
        return {}
    return decode(msg)
