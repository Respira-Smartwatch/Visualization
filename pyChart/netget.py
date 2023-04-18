import socket
import threading
import time

class NetGet:
    def __init__(self, connection_ip: str=None, connection_port: int=44444):
        self.ip = connection_ip if connection_ip else '140.9.9.9'
        self.port = connection_port
        self.socket = None
        self.connect()

    def connect(self):
        def make_sock():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((self.ip, self.port))
            self.socket=s
        
        sock = threading.Thread(target=make_sock)
        sock.start()
        seconds = 0

        while not self.socket and seconds<10 and sock.is_alive():
            seconds += 1
            time.sleep(1)
        
        if not self.socket:
            print("NO SOCKET CREATED")
            raise ConnectionError

    def read_data(self):
        if self.socket:
            print("GETTING?")
            return int(self.socket.recv(1))
        else:
            print("NO SOCKET - NO DATA")
            return -1

if __name__ == "__main__":
    ng = NetGet(connection_ip="140.182.152.100")
    while True:
        print(ng.read_data())
