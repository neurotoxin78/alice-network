#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import SOAPpy

server = SOAPpy.SOAPProxy("https://10.10.7.3:3333/")

resp = server.hello('neuro')
print resp
resp = server.ping()
print resp
resp = server.available_commands()
print resp





