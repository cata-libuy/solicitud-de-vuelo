from classes.user import User
from classes.role import Role
from classes.permission import Permission
from classes.employee import Employee

# name = raw_input('say your name...')
# print ('hello '+name)

# crea roles y permisos
admin = Role('Admin')
solicitante = Role('Solicitante')
aprobador = Role('Aprobador')
crearSolicitud = Permission('Solicitud', 'crear')
aprobarSolicitud = Permission('Solicitud', 'aprobar')
solicitante.add_permission(crearSolicitud)
aprobador.add_permission(aprobarSolicitud)
admin.add_permission(crearSolicitud)
admin.add_permission(aprobarSolicitud)

# crea usuarios
cata = Employee('Cata', 'Orellana', 'cata.libuy@gmail.com', '123123', 'Developer')
print(cata)
# pepito = User(2, 'Pepito', 'Perez', 'pepito@gmail.com', '123123')
# jefa = User(3, 'Juanita', 'Perez', 'juanita@gmail.com', '123123')
cata.add_role(admin)
# pepito.add_role(solicitante)
# jefa.add_role(aprobador)
print('role added')
