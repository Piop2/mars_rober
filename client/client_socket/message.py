from utils.json_data import encode, decode


def send(client, data):
    msg = encode(data)
    client.send(msg)
    return


def receive(server):
    msg = server.recv(1024)
    if not msg:
        return {}
    return decode(msg)
