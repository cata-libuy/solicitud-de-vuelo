class Airport(object):

    def __init__(self, id, airport_code, city):
        self.id = id
        self.airport_code = airport_code
        self.city = city

    def __str__(self):
        return self.airport_code
