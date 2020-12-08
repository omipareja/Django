from app.wsgi import *
from core.erp.models import Type, Employee

#Insertar pruebasssss

#t = Type()
#t.names ='prubaaaxdxdxdxdxd'
#t.save()

#Select
#query= Type.objects.all()
#print(query)

#Editar

#t = Type.objects.get(id=1)
#t.names ="AJAJAJAJJAJA"
#t.save()
#print(t.names)

#Borrar Datos
#t = Type.objects.get(id=1)
#t.delete()

#Listar con metodo filter para realizar flitros
#obj = Type.objects.filter(names__icontains='pre') #Contengan
#obj = Type.objects.filter(names__istartswith='P') #Inicien
#obj = Type.objects.filter(names__endswith='a') #Termine
obj = Type.objects.filter(names__endswith='a').exclude(id=5) #Contengan

print(obj)