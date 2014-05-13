from yapsy.IPlugin import IPlugin

class ping(IPlugin):

    def ping(self):
        return "pong"


