class Management(object):

    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.aproover = None

    def __str__(self):
        return self.name
