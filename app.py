# -*- coding: utf-8 -*-
import sys
# Clases entidad
from entity_classes.user import User
from entity_classes.role import Role
from entity_classes.permission import Permission
from entity_classes.employee import Employee
from entity_classes.travel_reason import TravelReason
from entity_classes.reason_type import ReasonType
from entity_classes.travel_request import TravelRequest
from entity_classes.project import Project
from entity_classes.department import Department
from entity_classes.management import Management
from entity_classes.aditional_need import AditionalNeed, HotelReservation, Taxi, CarRent
from entity_classes.airport import Airport
from entity_classes.journey import Journey
from entity_classes.journey_point import JourneyPoint
# Clases borde
from ui_classes.menu import Menu
from ui_classes.new_request_view import NewRequestView

# name = raw_input('say your name...')
# print ('hello '+name)

class App(object):

    def __init__(self):
        # entity_classes
        self.employees = []
        self.roles = {}
        self.travel_reasons = []
        self.travel_requests = []
        self.reason_types = []
        self.managements = []
        self.employee = None
        self.airports = []
        # control_clases
        self.menu = {}

        # run
        self.create_test_data()
        self.init_main_menu()

    def create_test_data(self):
        # crea datos de prueba base para poder usar el app
        print('Creando datos de prueba...')
        self._create_default_roles()
        self._create_default_employees()
        self._create_default_reason_types()
        self._create_default_organization()
        self._create_default_airports()
        print('---------------------------')
        self.employee = self.employees[0]
        print('simulando login con ' + str(self.employee))
        print('')

    def init_main_menu(self):
        items = [
            { 'text': 'Solicitud de Vuelo', 'action': self.init_travel_submenu },
            { 'text': 'Salir', 'action': sys.exit }
        ]
        self.menu = Menu('MENÚ PRINCIPAL', items)
        self.menu.displayMenu()

    def init_travel_submenu(self):
        items = [
            { 'text': 'Nueva Solicitud', 'action': self.new_travel_request },
            { 'text': 'Volver', 'action': self.init_main_menu }
        ]
        self.menu = Menu('SUB MENÚ SOLICITUD DE VUELO', items)
        self.menu.displayMenu()

    def new_travel_request(self):
        newId = len(self.travel_requests) + 1
        view = NewRequestView(self.reason_types, self.employee, self.managements, self.airports)
        new_request = view.new_request(newId)
        if (new_request):
            self.travel_requests.append(new_request)
            print('')
            print('Nueva Solicitud creada:')
            print(new_request.print_request())
        else:
            print('Ocurrió un error al crear solicitud')

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
        gerente = self.employees[2]
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

    def _create_default_airports(self):
        airport_conce = Airport(1, 'C1', 'Concepción')
        airport_stgo = Airport(2, 'S1', 'Santiago')
        self.airports = [ airport_conce, airport_stgo ]
        print('Aeropuertos creados')

# run app!
app = App()
