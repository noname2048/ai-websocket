# udp python pure server
import socket
import datetime
import jwt

# jwt info
key = "abcdefghijklmnop"

# socket info
host: str = '127.0.0.1'
port: int = 8030

# timezone info
KST = datetime.timezone(datetime.timedelta(hours=9))

def now() -> str:
    """현재시각을 timezone 'Asia/Seoul', UTC+9 형태의 str로 반환하는 함수"""
    _now = datetime.datetime.now(tz=KST)
    return _now.strftime("%Y-%m-%d %H:%M:%S")

def validate_token(token: str):
    jwt.decode(jwt=token, key=key, algorithms=["HS256"])
    

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    try:
        sock.bind((host, port))
        print("--- ready for recv data ---")

        while True:
            data, addr = sock.recvfrom(1024)
            print(f'[{now()}] from({addr[0]}:{addr[1]}), receved: {data.decode()}')
            d = jwt.decode(jwt=data, key=key, algorithms="HS256")
            print(d)
            
    except KeyboardInterrupt as e:
        print("--- udp server ended successful ---")


