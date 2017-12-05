
from threading import Thread
from node import Node
from channel import Channel

class Iface:
    def __init__(self, node, num):
        self.node = node
        self.id = node.id + '.' + num
        self.running = True
        self.channel = Channel()

        self.link = None

    """
    Thread
    """
    def __processQueue(self):
        """
        Funcio que s'executa tota la estona per tal de poder rebre missatges.
        """
        while self.running:
            message = self.channel.receive()
            self.node.receive(message, self.id)


    """
    Linking
    """
    def set_link(self, iface):
        self.link = iface

    def is_linked(self):
        return self.link != None

    def send(self, msg):
        """
        Funci que serveix per enviar un missatge desde aquesta iface
        """
        if self.is_linked():
            self.link.channel.send(msg)
        else:
            print("is not linked")

    """
    Thread tractment
    """
    def run(self):
        """
        Genera un thread per a cada interficie. Aquest thread creida a la funcio
        __processQueue, el qual esta pendent de rebre missatges.
        """
        self.thread = Thread(target=self.__processQueue)
        self.thread.start()

    def stop(self):
        self.running = False

    """
    Printing
    """
    def __str__(self):
        return 'Iface %s' % (self.id)

    def __repr__(self):
        return 'Iface(id=%s)' % (self.id)
