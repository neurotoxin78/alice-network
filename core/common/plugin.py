#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path , listdir
root_path = path.dirname(path.realpath(__file__))[:-11]
import logging
logFormatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

PluginFolder = root_path + 'plugins'
MainModule = "__init__"
#sys.path.append(PluginFolder)

class plugin_manager(object):

    """Docstring for plugin. """

    def __init__(self):
        """@todo: to be defined1. """



