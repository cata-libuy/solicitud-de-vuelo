from classes.user import User
from classes.role import Role
from classes.permission import Permission
from classes.employee import Employee

# name = raw_input('say your name...')
# print ('hello '+name)

# crea roles
admin = Role(1, 'Admin')
solicitante = Role(2, 'Solicitante')
aprobador = Role(3, 'Aprobador')
# crea permisos
crear_solicitud = Permission(1, 'crear solicitud')
aprobar_solicitud = Permission(2, 'aprobar solicitud')
# agrega permisos a roles
solicitante.add_permission(crear_solicitud)
aprobador.add_permission(aprobar_solicitud)
admin.add_permission(crear_solicitud)
admin.add_permission(aprobar_solicitud)

# crea usuarios
cata = Employee(1, 'Cata', 'Orellana', 'cata.libuy@gmail.com', '123123', 'Developer')
print(cata)
pepito = Employee(2, 'Pepito', 'Perez', 'pepito@gmail.com', '123123', 'Ingeniero')
jefa = Employee(3, 'Juanita', 'Perez', 'juanita@gmail.com', '123123', 'Jefe')

# asigna roles
cata.add_role(admin)
pepito.add_role(solicitante)
jefa.add_role(aprobador)
print('roles added')
