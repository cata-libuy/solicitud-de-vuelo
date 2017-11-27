# -*- coding: utf-8 -*-
class AditionalNeed(object):
    def __init__(self, id, type = None, comments = ''):
        self.id = id
        self.type = type
        self.comments = comments

    def __str__(self):
        if self.type:
            return self.type
        else:
            return 'Tipo no definido'

class HotelReservation(AditionalNeed):
    def __init__(self, id, comments = '', nights = 0):
        type = 'Reserva de Hotel'
        super(HotelReservation, self).__init__(id, type, comments)
        self.nights = nights

    def __str__(self):
        return self.type

class Taxi(AditionalNeed):
    def __init__(self, id, comments = '', from_address = '', to_address = ''):
        type = 'Taxi'
        super(Taxi, self).__init__(id, type, comments)
        self.from_address = from_address
        self.to_address = to_address

    def __str__(self):
        return self.type

class CarRent(AditionalNeed):
    def __init__(self, id, comments = '', vehicle_type = '', days = 1):
        type = 'Arriendo de Vehículo'
        super(CarRent, self).__init__(id, type, comments)
        self.vehicle_type = vehicle_type
        self.days = days

    def __str__(self):
        return self.type
