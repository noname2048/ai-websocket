# 센서를 흉내내는 코드
# 센서는 UDP send를 반복한다.

import socket
import time
import datetime

host: int = "127.0.0.1"
port: str = 8030
data = "Hello World"

def now() -> str:
    _now = datetime.datetime.now()
    return _now.strftime("%Y-%m-%d %H:%M:%S")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(("127.0.0.1", port))

    try:
        while True:
            print(f"[{now()}] to({host}:{port}), send: {data}")
            sock.sendall(data.encode())
            time.sleep(5)

    except KeyboardInterrupt as e:
        print("sensor end")
