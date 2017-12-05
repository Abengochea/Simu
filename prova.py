from context import set_context
from iface import Iface
from node import Node

if __name__ == "__main__":
    set_context()
    x = Node("wea")
    iface_x = Iface(x, "123")
    iface_x.run()
    x.set_iface(iface_x)
    iface_x.send("hello world")

    print("Running")
