from threading import Thread

class Node:

    def __init__(self, id):
        self.id = id
        self.running = True
        self.iface_list = []

    def is_alive(self):
        return self.running

    def receive(self, msg, iface):
        """
        Definir que fer amb el missatge que rebem per la interfici
        """
        print(msg+iface)

    def send(self, msg, dest):
        print("wea")

    def set_iface(self, iface):
        iface.run()
        self.iface_list.append(iface)

    def remove_iface(self, iface):
        iface.stop()
        self.iface_list.remove(iface)

