# 센서를 흉내내는 코드
# 센서는 UDP send를 반복한다.

import socket
import time
import datetime
import jwt # pyjwt

# jwt info
key = 'abcdefghijklmnop'

# network info
host: int = "127.0.0.1"
port: str = 8030

# timezone info
KST = datetime.timezone(datetime.timedelta(hours=9))

def now() -> str:
    """현재시각을 timezone 'Asia/Seoul', UTC+9 형태의 str로 반환하는 함수"""
    _now = datetime.datetime.now(tz=KST)
    return _now.strftime("%Y-%m-%d %H:%M:%S")

def create_token(temperature: str, humidity: str) -> bytes:
    """온습도를 jwt 변환한뒤 바이트코드 변환하여 송신용 데이터를 생성하는 함수"""
    payload = {
        'temperature': temperature,
        'humidity': humidity,
    }
    print(payload)
    encoded: str = jwt.encode(payload=payload, key=key, algorithm="HS256")
    return encoded.encode()

# socket algorithm

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(("127.0.0.1", port))
    
    try:
        data: bytes = create_token("26.7", "60.3")
        print("Data send start, if you want to stop press Ctrl+C")

        while True:
            print(f"[{now()}] to({host}:{port}), send: {data}")
            sock.sendall(data)
            time.sleep(5)

    except KeyboardInterrupt as e:
        print("Data send ended.")
