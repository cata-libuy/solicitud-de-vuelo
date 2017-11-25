from user import User

class Employee(User):
    def __init__(self, name, last_name, email, password, cargo):
        super(Employee, self).__init__(name, last_name, email, password)
        self.cargo = cargo

    def __str__(self):
        return super(Employee, self).__str__() + ', ' + self.cargo
