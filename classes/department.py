class Department(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def add_aproover(self, aproover):
        self.aproover = aproover
