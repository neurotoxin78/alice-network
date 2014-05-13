#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from types import MethodType
root_path = path.dirname(path.realpath(__file__))
from handlers.base import base_commands
from SOAPpy import ThreadingSOAPServer
from M2Crypto import SSL
from M2Crypto import threading    
from yapsy.PluginManager import PluginManager 
import logging
PluginFolder = root_path[:-4] + 'plugins'
import inspect

logFormatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

## Globals
global commands

if __name__ == '__main__':
    threading.init()
    ssl_context = SSL.Context()
    ssl_context.load_cert('../certificates/server.pem')

    ## Loading Plugins
    print 'Loading plugins in ' + PluginFolder 
    Manager = PluginManager()
    Manager.setPluginPlaces(PluginFolder)
    Manager.collectPlugins()
    commands = base_commands()
        
    for plugin in Manager.getAllPlugins():
        Manager.activatePluginByName(plugin.name)
        for i in inspect.getmembers(plugin.plugin_object, predicate=inspect.ismethod):
            if 'activate' not in i[0]:
                if '__init__' not in i[0]:
                    setattr(commands, i[0], i[1])
                    print "Add plugin: ", i[0]
    print 'Plugins loaded sucesfully\n Start listening on port 3333'
    server = ThreadingSOAPServer(("0.0.0.0",3333), ssl_context = ssl_context)
    server.registerObject(commands)
    server.serve_forever()


