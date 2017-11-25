class TravelRequest(object):

    def __init__(
        self,
        id,
        solicitant,
        aprooved = False,
        department = None,
        description = '',
        journey = None,
        reason = None,
        special_needs = [],
        passengers = [],
        urgent = False ):
        self.id = id
        self.solicitant = solicitant
        self.aprooved = aprooved
        self.department = department
        self.description = description
        self.journey = journey
        self.reason = reason
        self.special_needs = special_needs
        self.passengers = passengers
        self.urgent = urgent

    def __str__(self):
        return str(self.id) + ', ' + self.description

    def set_solicitant(self, solicitant):
        self.solicitant = solicitant

    def set_management(self, management):
        self.management = management

    def set_department(self, department):
        self.department = department

    def set_aprooved(self, aprooved):
        self.aprooved = aprooved

    def set_description(self, description):
        self.description = description

    def set_journey(self, journey):
        self.journey = journey

    def set_reason(self, reason):
        self.reason = reason

    def set_special_needs(self, special_needs):
        self.special_needs = special_needs

    def set_passengers(self, passengers):
        self.passengers = passengers

    def set_urgent(self, urgent):
        self.urgent = urgent
