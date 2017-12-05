import types
import sys
import os.path

import util

core_type = None
available_types = ['thread', 'green_thread']


def set_context(module_name='thread'):
    '''
    This function initializes the context of execution deciding which
    type of threads are being used: classic python threads or green
    threads, provided by Gevent.
    This should be called first of all in every execution, otherwise,
    the library would not work.
    The default module is 'thread'.
    :param str. module_name: Name of the module you want to use
        ('thread' or 'green_thread').
    '''
    global core_type
    if core_type is None and module_name in available_types:
        core_type = module_name
        util.core_type = core_type
        global iface
        iface = __import__('ospf.' + module_name + '.iface', globals(),
                           locals(), ['Iface'], 0)

        if module_name == 'green_thread':
            signal = __import__('gevent', ['signal'])
        else:
            signal = __import__('signal', ['signal'])
    else:
        raise Exception('Bad core type.')
