from yapsy.IPlugin import IPlugin

class hello(IPlugin):

    def hello(self, name):
        return "hello " + name


