from django.db import models
from django.forms import ModelForm
# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=70)

class Producto(models.Model):
    nombre= models.CharField(max_length=80)
    categoria = models.ForeignKey(Categoria, related_name='categorias', on_delete=models.CASCADE)
    unidades = models.IntegerField()
    valorMonetario = models.FloatField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre