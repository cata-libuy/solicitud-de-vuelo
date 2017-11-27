class TravelReason(object):
    def __init__(self, id, reason_type, comments = '', hour = '', receiver = None):
        self.id = id
        self.reason_type = reason_type
        self.comments = comments
        self.hour = hour
        self.receiver = receiver

    def __str__(self):
        return str(self.reason_type) + ', ' + ' con ' + self.receiver + ', ' + self.comments
