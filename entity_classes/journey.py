class Journey(object):
    def __init__(self, id, origin = None, destination = None, estimated_arrival = None):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.estimated_arrival = estimated_arrival

    def __str__(self):
        if (self.origin and self.destination):
            return 'De %s a %s' % (str(self.origin), str(self.destination),)
        else:
            return 'Origen y destino no definidos'
