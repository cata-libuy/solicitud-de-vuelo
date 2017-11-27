from user import User

class Employee(User):
    def __init__(self, id, name, last_name, email, password, cargo):
        # inicializo super
        super(Employee, self).__init__(id, name, last_name, email, password)
        self.id = id
        self.cargo = cargo

    def __str__(self):
        return super(Employee, self).__str__() + ', ' + str(self.cargo)
