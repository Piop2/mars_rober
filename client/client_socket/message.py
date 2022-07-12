import utils


def send(client, data):
    msg = utils.json_data.encode(data)
    client.send(msg)
    return


def receive(server):
    msg = server.recv(1024)
    if not msg:
        return {}
    return utils.json_data.decode(msg)
