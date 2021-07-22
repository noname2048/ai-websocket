# udp python pure server
import socket
import datetime

host: str = '127.0.0.1'
port: int = 8030

def now() -> str:
    _now = datetime.datetime.now()
    return _now.strftime("%Y-%m-%d %H:%M:%S")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    try:
        sock.bind((host, port))
        print("--- ready for recv data ---")

        while True:
            data, addr = sock.recvfrom(1024)
            print(f'[{now()}] from({addr[0]}:{addr[1]}), receved: {data.decode()}')
            
    except KeyboardInterrupt as e:
        print("--- udp server ended successful ---")


