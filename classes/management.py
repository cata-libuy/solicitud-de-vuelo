class Management(object):

    def __init__(self, id, name, aproover = None):
        self.name = name
        self.id = id
        self.aproover = aproover
        self.departments = []

    def __str__(self):
        return self.name

    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department) 
