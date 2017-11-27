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

    def get_aproovers(self, department = None, project = None):
        aproovers = [ self.aproover, ]
        if department and department.aproover and department.aproover not in aproovers:
            aproovers.append(department.aproover)
        if project and project.aproover and project.aproover not in aproovers:
            aproovers.append(project.aproover)
        return aproovers
