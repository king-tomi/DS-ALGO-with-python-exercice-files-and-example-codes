author = "Ayodabo Tomisin Kolawole"
date_created = "2020-08-09"
file_description = """ds and algo with python chapter 1 exercise P2-3.5"""


import time

class Process:
    """System to simulate transfer process"""

    def __init__(self,sender,receiver):
        self._sender = sender
        self._receiver = receiver

    def process(self):
        """processes the packets"""
        packets = self._sender.send_packets()
        if packets:
            time.sleep(2)
            self._receiver.receive_packets(packets)
            print("Packets sent amd received successfully")
        else:
            print("ERROR! packets are not available")


class Sender:

    def __init__(self,name: str,packets=None,state=False):
        self._name = name
        self._packets = packets
        self._state = state

    @property
    def name(self) -> str:
        return self._name

    @property
    def packets(self):
        return self._packets
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self,val: bool):
        self._state = val

    def check_packets(self) -> bool:
        return self._packets is None

    def send_packets(self):
        if self.check_packets():
            self.state = True
            return self.packets
        else:
            return None

    def __str__(self):
        return f"{self.name} is a sender"

    def __repr__(self):
        return f"<Sender {self.name}>"

class Receiver:

    def __init__(self,name: str,packets=None):
        self._name = name
        self._packets = packets

    @property
    def name(self):
        return self._name

    @property
    def packets(self):
        return self._packets

    @packets.setter
    def packets(self,val):
        self._packets = val

    def receive_packets(self,packets):
        self.packets = packets

    def open_packets(self):
        if not (self.packets is None):
            with open(self.packets,"r") as pack:
                for line in pack.readlines():
                    print(line.strip("\n"))