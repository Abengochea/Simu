from threading import Thread
from node import Node
from channel import Channel

class Iface:
    def __init__(self, node, addr_iface):
        self.node = node
        self.addr_iface = addr_iface
        self.running = True
        self.channel = Channel()

    def __processQueue(self):
        """
        Funcio que s'executa tota la estona per tal de poder rebre missatges.
        """
        while self.running:
            message = self.channel.receive()
            self.node.receive(message, self.addr_iface)

    def send(self, msg):
        """
        Funci que serveix per enviar un missatge desde aquesta iface
        """
        self.channel.send(msg)

    def run(self):
        """
        Genera un thread per a cada interficie. Aquest thread creida a la funcio
        __processQueue, el qual esta pendent de rebre missatges.
        """
        self.thread = Thread(target=self.__processQueue)
        self.thread.start()
