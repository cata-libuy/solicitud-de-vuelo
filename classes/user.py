class User(object):
    def __init__(self, id, name, last_name, email, password):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.roles = []
        self.password = password

    def __str__(self):
        return self.name + ' ' + self.last_name

    def add_role(self, role):
        self.roles.append(role)

    def has_role(self, role):
        return role in self.roles
