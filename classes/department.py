class Department(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.aproover = None

    def __str__(self):
        return self.name

    def add_aproover(self, aproover):
        self.aproover = aproover
