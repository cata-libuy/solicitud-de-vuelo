# -*- coding: utf-8 -*-

from entity_classes.travel_request import TravelRequest
from entity_classes.travel_reason import TravelReason

class NewRequestView(object):

    def __init__(self, reason_types):
        self.reason_types = reason_types
        self.request = None
        print('')

    def new_request(self, id, solicitant):
        self.id = id
        self.request = TravelRequest(id, solicitant)
        print('----Nueva Solicitud de Vuelo----')
        description = raw_input('Ingrese descripción... ')
        self.request.set_description(description)
        reason = self._choose_reason()
        self.request.set_reason(reason)
        return self.request

    def _choose_reason(self):
        reason_type = None
        comments = None
        hour = None
        receiver = None

        print('Motivos')
        while reason_type is None:
            counter = 1
            for reason in self.reason_types:
                print(str(counter) + '. ' + str(reason))
                counter += 1
            choice = int(raw_input('Elija un motivo... '))
            if type(choice) is int and choice > 0 and choice <= len(self.reason_types):
                reason_type = self.reason_types[choice - 1]
            else:
                print('Opción inválida')

        hour = raw_input('Ingrese hora de la reunión... ')
        receiver = raw_input('Ingrese con quién se reunirá... ')
        comments = raw_input('Ingrese comentarios... ')
        return TravelReason(self.id, reason_type, comments, hour, receiver)
