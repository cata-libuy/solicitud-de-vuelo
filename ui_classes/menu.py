# -*- coding: utf-8 -*-
class Menu(object):
    def __init__(self, name, items = []):
        self.name = name
        self.items = items

    def displayMenu(self):
        print('')
        print(self.name)
        count = 1
        for menu_item in self.items:
            print('%s. %s' % (count, menu_item.text))
            count += 1
        option = int(raw_input('Ingrese opción de menu...'))
        self._handle_input(option)

    def _handle_input(self, option):
        if type(option) is int and option > 0 and option <= len(self.items):
            self.items[option - 1].action()
        else:
            print('Opción inválida')
            self.displayMenu
