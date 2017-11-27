class Department(object):

    def __init__(self, id, name, aproover = None, projects = []):
        self.id = id
        self.name = name
        self.aproover = aproover
        self.projects = []

    def __str__(self):
        return self.name

    def add_aproover(self, aproover):
        self.aproover = aproover
