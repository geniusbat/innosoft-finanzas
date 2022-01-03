from django.db import models

class tipoSugerencia(models.TextChoices):
        tecnica = "tecnica"
        sugerenciaInnosoft = "sugerenciaInnosoft"

class Sugerencia(models.Model):
        sugTipo = models.CharField(choices=tipoSugerencia.choices, default=tipoSugerencia.tecnica.name, max_length=25)
        uvus = models.CharField(max_length=10)
        description = models.CharField(max_length=1000)