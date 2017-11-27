# -*- coding: utf-8 -*-

from entity_classes.travel_request import TravelRequest
from entity_classes.travel_reason import TravelReason

class NewRequestView(object):

    def __init__(self, reason_types, solicitant, managements):
        self.reason_types = reason_types
        self.solicitant = solicitant
        self.managements = managements
        self.request = None
        print('')

    def new_request(self, id):
        self.id = id
        self.request = TravelRequest(id, self.solicitant)
        print('----Nueva Solicitud de Vuelo----')
        description = raw_input('Ingrese descripción... ')
        self.request.set_description(description)
        reason = self._choose_reason()
        self.request.set_reason(reason)
        return self.request

    def _choose_reason(self):
        reason_type = self._select_option(self.reason_types, 'Motivos', 'Elija un motivo... ')
        hour = raw_input('Ingrese hora de la reunión... ')
        receiver = raw_input('Ingrese con quién se reunirá... ')
        comments = raw_input('Ingrese comentarios... ')
        return TravelReason(self.id, reason_type, comments, hour, receiver)

    # def _choose_aproover(self):
        # elegir gerencia
        # elegir departamentos
        # elegir proyecto
        # elegir aprobador

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
