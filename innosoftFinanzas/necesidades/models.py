from django.db import models
from inventario.models import Producto

# Create your models here.

class Comite(models.Model):
    comite = models.CharField(max_length=70, unique=True)

class Necesidad(models.Model):
    nombre= models.CharField(max_length=80)
    cantidadNecesitada= models.IntegerField()
    comite= models.ForeignKey(Comite, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre