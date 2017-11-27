class MenuItem(object):
    def __init__(self, text = '', action = None):
        self.text = text
        self.action = action

    def __str__(self):
        return self.text
