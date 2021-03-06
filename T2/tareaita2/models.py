from django.db import models


class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    precio = models.IntegerField(blank=False)
    descripcion = models.CharField(max_length=100, blank=False)
    imagen = models.URLField(blank=False)
    ingredientes = models.ManyToManyField("Ingrediente", blank=True)


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

