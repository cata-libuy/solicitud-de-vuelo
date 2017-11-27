# -*- coding: utf-8 -*-

from entity_classes.travel_request import TravelRequest
from entity_classes.travel_reason import TravelReason
from entity_classes.journey import Journey
from entity_classes.journey_point import JourneyPoint

class NewRequestView(object):

    def __init__(self, reason_types, solicitant, managements, airports):
        self.reason_types = reason_types
        self.solicitant = solicitant
        self.managements = managements
        self.request = None
        self.airports = airports
        print('')

    def new_request(self, id):
        self.id = id
        self.request = TravelRequest(id, self.solicitant)
        print('----Nueva Solicitud de Vuelo----')
        self.request.set_description(raw_input('Ingrese descripción... '))
        self.request.set_reason(self._choose_reason())
        self.request.set_aproover(self._choose_aproover())
        self.request.set_journey(self._choose_journey())
        return self.request

    def _choose_reason(self):
        reason_type = self._select_option(self.reason_types, 'Motivos', 'Elija un motivo... ')
        hour = raw_input('Ingrese hora de la reunión... ')
        receiver = raw_input('Ingrese con quién se reunirá... ')
        comments = raw_input('Ingrese comentarios... ')
        return TravelReason(self.id, reason_type, comments, hour, receiver)

    def _choose_aproover(self):
        selected_management = self._select_option(self.managements, 'Gerencias', 'Elija una gerencia... ')
        selected_department = self._select_option(selected_management.departments, 'Departamentos', 'Elija un departamento... ')
        selected_project = None
        if len(selected_department.projects) > 0:
            selected_project = self._select_option(selected_department.projects, 'Proyectos', 'Elija un proyecto... ')
        aproovers = selected_management.get_aproovers(selected_department, selected_project)
        selected_aproover = self._select_option(aproovers, 'Aprobador', 'Elija un aprobador... ')
        return selected_aproover

    def _choose_journey(self):
        o_airport = None
        d_airport = None
        while o_airport == d_airport:
            o_airport = self._select_option(self.airports, 'Aeropuertos', 'Ingrese aeropuerto de origen... ')
            d_airport = self._select_option(self.airports, 'Aeropuertos', 'Ingrese aeropuerto de destino... ')
            if o_airport == d_airport:
                print('Origen y destino no pueden ser iguales')
        o_date = raw_input('Ingrese fecha de salida... ')
        o_hour = raw_input('Ingrese hora de salida si desea... ')
        # origen y destino
        origin = JourneyPoint(self.id, o_airport, o_date, o_hour)
        destiny = JourneyPoint(self.id, d_airport)
        # Regreso
        arrival = raw_input('Ingrese fecha de regreso estimado... ')
        return Journey(self.id, origin, destiny, arrival)

    def _select_option(self, options, title, message):
        choosen_option = None
        counter = 1
        print(title)
        while not choosen_option:
            for option in options:
                print(str(counter) + '. ' + str(option))
                counter += 1
            choice = int(raw_input(message))
            if type(choice) is int and choice > 0 and choice <= len(options):
                choosen_option = options[choice - 1]
                return choosen_option
            else:
                print('Opción inválida')
