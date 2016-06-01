from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

TIPO_SALDO_CHOICES = (
                     ('d', 'Debito'),
                     ('c', 'Credito')
)

class Fuente(models.Model):
    nombre = models.CharField(max_length=200)
    naturaleza = models.IntegerField(default=0)
    fecha = models.DateTimeField('fecha')

class Tercero(models.Model):
    nombre = models.CharField(max_length=200)
    identificacion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    fecha = models.DateTimeField('fecha')


class Clase(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    tipo_de_saldo = models.CharField(max_length=1, choices=TIPO_SALDO_CHOICES)
    def __unicode__(self):
        return self.nombre


class Grupo(models.Model):
    nombre = models.CharField(max_length=40)
    clase = models.ForeignKey(Clase)
    def __unicode__(self):
        if self.clase.tipo_de_saldo == 'd':
            columna = 'Debe - '
        elif self.tipo.tipo_de_saldo == 'c':
            columna = 'Credito - '
        return columna + str(self.tipo) + ' - ' + str(self.nombre)
    class Meta:
        unique_together = (("nombre", "clase"),)

class Cuenta(models.Model):
    nombre = models.CharField(max_length=40)
    grupo = models.ForeignKey(Grupo)
    def __unicode__(self):
        return str(self.grupo) + ' - ' + str(self.nombre)
    class Meta:
        unique_together = (("nombre", "grupo"),)

class Asiento(models.Model):
    fuente = models.ForeignKey(Fuente, on_delete=models.CASCADE)
    tercero = models.ForeignKey(Tercero, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    referencia = models.IntegerField(default=0)
    debito = models.FloatField(default=0)
    credito = models.FloatField(default=0)
    fecha = models.DateTimeField('fecha')
