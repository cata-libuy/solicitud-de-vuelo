# -*- coding: utf-8 -*-
from classes.user import User
from classes.role import Role
from classes.permission import Permission
from classes.employee import Employee
from classes.travel_reason import TravelReason
from classes.reason_type import ReasonType
from classes.travel_request import TravelRequest
from classes.project import Project
from classes.department import Department
from classes.management import Management
from classes.aditional_need import AditionalNeed, HotelReservation, Taxi, CarRent

# name = raw_input('say your name...')
# print ('hello '+name)

class App(object):

    def __init__(self):
        self.employees = []
        self.roles = {}
        self.travel_reasons = []
        self.travel_requests = []
        self.reason_types = []
        self.managements = []
        self.create_test_data()

    def create_test_data(self):
        # crea datos de prueba base para poder usar el app
        print('Creando datos de prueba...')
        self._create_default_roles()
        self._create_default_employees()
        self._create_default_reason_types()
        self._create_default_organization()

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
        pepito = Employee(2, 'Pepito', 'Pepes', 'pepito@gmail.com', '123123', 'Ingeniero')
        gerente1 = Employee(3, 'Juanita', 'Perez', 'juanita@gmail.com', '123123', 'Gerente Proyectos')
        jefe1 = Employee(4, 'Federico', 'Federer', 'fede@gmail.com', '123123', 'Jefe Proyecto 1')
        jefe2 = Employee(5, 'Anastacio', 'Flores', 'tacito@gmail.com', '123123', 'Jefe Proyecto 2')

        # asigna roles
        cata.add_role(self.roles['admin'])
        pepito.add_role(self.roles['solicitante'])
        gerente1.add_role(self.roles['aprobador'])
        jefe1.add_role(self.roles['aprobador'])
        jefe2.add_role(self.roles['aprobador'])
        self.employees = [ cata, pepito, gerente1, jefe1, jefe2 ]
        print('Trabajadores creados:')
        for employee in self.employees:
            print(' -' + str(employee))

    def _create_default_reason_types(self):
        reunion = ReasonType(1, 'Reunión')
        otro = ReasonType(2, 'Otro')
        self.reason_types = [ reunion, otro ]
        print('Tipos de motivo creados')

    def _create_default_organization(self):
        gerente = self.employees[3]
        gerencia_proyectos = Management(1, 'Gerencia de Proyectos', gerente)
        jefe1 = self.employees[3]
        jefe2 = self.employees[4]
        depto1 = Department(1, 'Depto proyectos 1', jefe1)
        depto2 = Department(2, 'Depto proyectos 2', jefe2)
        gerencia_proyectos.add_department(depto1)
        gerencia_proyectos.add_department(depto2)
        self.managements.append(gerencia_proyectos)
        print('Gerencia creada:')
        print(str(self.managements[0]))
        print('con departamentos')
        for depto in self.managements[0].departments:
            print(' -' + str(depto))





# run app!
app = App()
