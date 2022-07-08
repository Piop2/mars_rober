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
    data = decode(msg)

    # camera bytes 에 있는 이미지 파일은 따로 디코딩
    data['camera']['bytes'] = decode_image(data['camera']['bytes'])
    return data
