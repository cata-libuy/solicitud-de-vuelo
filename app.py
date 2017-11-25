# -*- coding: utf-8 -*-
from classes.user import User
from classes.role import Role
from classes.permission import Permission
from classes.employee import Employee
from classes.travel_reason import TravelReason
from classes.reason_type import ReasonType
from classes.travel_request import TravelRequest

# name = raw_input('say your name...')
# print ('hello '+name)

class App(object):

    def __init__(self):
        self.employees = []
        self.roles = {}
        self.travel_reasons = []
        self.travel_requests = []
        self.reason_types = []
        self.create_test_data()

    def create_test_data(self):
        # crea datos de prueba base para poder usar el app
        print('Creando datos de prueba...')
        self._create_default_roles()
        self._create_default_employees()
        self._create_default_reason_types()

    def _create_default_roles(self):
        # crea roles
        admin = Role(1, 'Admin')
        solicitante = Role(2, 'Solicitante')
        aprobador = Role(3, 'Aprobador')

        # crea permisos
        crear_solicitud = Permission(1, 'crear solicitud')
        aprobar_solicitud = Permission(2, 'aprobar solicitud')

        # agrega permisos a roles
        solicitante.add_permission(crear_solicitud)
        aprobador.add_permission(aprobar_solicitud)
        admin.add_permission(crear_solicitud)
        admin.add_permission(aprobar_solicitud)
        self.roles = { 'admin': admin, 'solicitante': solicitante, 'aprobador': aprobador }
        print('Roles creados:')
        for role in self.roles.keys():
            print(' -' + str(self.roles[role]))

    def _create_default_employees(self):
        # crea trabajadores
        cata = Employee(1, 'Cata', 'Orellana', 'cata.libuy@gmail.com', '123123', 'Developer')
        pepito = Employee(2, 'Pepito', 'Perez', 'pepito@gmail.com', '123123', 'Ingeniero')
        jefa = Employee(3, 'Juanita', 'Perez', 'juanita@gmail.com', '123123', 'Jefe')

        # asigna roles
        cata.add_role(self.roles['admin'])
        pepito.add_role(self.roles['solicitante'])
        jefa.add_role(self.roles['aprobador'])
        self.employees = [ cata, pepito, jefa ]
        print('Trabajadores creados:')
        for employee in self.employees:
            print(' -' + str(employee))

    def _create_default_reason_types(self):
        reunion = ReasonType(1, 'Reunión')
        otro = ReasonType(2, 'Otro')
        self.reason_types = [ reunion, otro ]
        print('Tipos de motivo creados')

# run app!
app = App()
