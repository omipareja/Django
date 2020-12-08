from django.db import models
from datetime import datetime
# Create your models here.
# Los modelos son para  crear las bases de datos

class Type(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Category(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        db_table = 'Categoria'


class Employee(models.Model):#Heredo de la clase modelo
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type,on_delete=models.CASCADE) #Relacion BAse de datos
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10,unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_created = models.DateTimeField(auto_now=True) # LA primera vez va tener la fecha actual despues no
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
    state = models.BooleanField(default=True)
   # gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d',null=True,blank=True)
    cvitae = models.FileField(upload_to='cvitae/%y/%m/%d',null=True,blank=True)


    def __str__(self): #Atributo que va representar este objeto
        return self.names

    class Meta:
        verbose_name ='Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']





