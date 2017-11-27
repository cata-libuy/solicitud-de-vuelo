class Department(object):

    def __init__(self, id, name, aproover = None):
        self.id = id
        self.name = name
        self.aproover = aproover

    def __str__(self):
        return self.name

    def add_aproover(self, aproover):
        self.aproover = aproover
