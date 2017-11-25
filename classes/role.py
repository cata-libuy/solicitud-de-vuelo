class Role(object):
    def __init__(self, name):
        self.name = name
        self.permissions = []

    def __str__(self):
        return self.name

    def add_permission(self, permission):
        self.permissions.append(permission)

    def has_permission(permission):
        return permission in self.permissions
