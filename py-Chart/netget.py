from pyp2p.net import Net

class NetGet:
    def __init__(self, connection_ip: str=None, connection_port: int=44444):
        if not connection_ip:
            return -1

        self.alice = Net(passive_bind=connection_ip, passive_port=connection_port, debug=1)
        self.alice.start()
        self.alice.bootstrap()
        self.alice.advertise()

    def read_data(self):
        for con in self.alice:
            for reply in con:
                print(reply)


if __name__ == "__main__":
    ng = NetGet(connection_ip="140.182.152.100")