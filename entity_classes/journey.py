class Journey(object):
    def __init__(self, id, origin = None, destiny = None, estimated_arrival = None):
        self.id = id
        self.origin = origin
        self.destiny = destiny
        self.estimated_arrival = estimated_arrival

    def __str__(self):
        if (self.origin and self.destiny):
            return 'De %s a %s' % (str(origin), str(destiny),)
        else:
            return 'Origen y destino no definidos'
