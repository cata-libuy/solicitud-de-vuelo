class JourneyPoint(object):
    def __init__(self, id, airport = None, estimated_date = None, estimated_hour = None):
        self.id = id
        self.airport = airport
        self.estimated_date = estimated_date
        self.estimated_hour = estimated_hour

    def __str__(self):
        return str(self.airport)
