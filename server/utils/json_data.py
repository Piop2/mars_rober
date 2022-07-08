import json


def encode(data):
    jsons = f"{json.dumps(data)}/"
    json_encode = jsons.encode()
    return json_encode


def decode(data):
    jsons = data.decode().split('/')[-2]
    data = json.loads(jsons)
    return data
