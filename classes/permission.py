class Permission(object):
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __str__(self):
        return self.name + ': ' + self.action
