#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path 
root_path = path.dirname(path.realpath(__file__))[:-8]
PluginFolder = root_path[:-5] + 'plugins'

import sys  
import logging
logFormatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


class base_commands(object):

    """Docstring for base_commands. """

    def __init__(self):
        """@todo: to be defined1. """
                           
            #print sys.modules.keys()
    
    def available_commands(self):
        """@todo: Docstring for available_commands.
        :returns: @todo

        """
        return self.__dict__


     





