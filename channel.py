import sys
from queue import Queue

class Channel(Queue):
    """
    Channel representa una interfici per als nodes, el qual permet rebre
    i enviar missatges. Realment es un simple facade de la class Queue de
    python.
    """

    def __init__(self):
        Queue.__init__(self)

    def send(self, msg):
        """ Envia un missatge a la interficie actual

        :param msg: El missatge que es vol enviar.
        """

        self.put(msg)

    def receive(self, timeout=None):
        """ Rep un missatge del canal, bloquejant el thread fins
        que es revi una resposta o salti el timeout

        :param int timeout: timeout per als missatges. Si no hi ha
            es bloqueja fins que arribi un
        :return: retorna el missatge enviat al canal.
        """

        return self.get(timeout=timeout)
