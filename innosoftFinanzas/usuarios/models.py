from django.db import models



class Roles(models.TextChoices):
        NA = "NA","NADA"
        MB = "MB","MIEMBRO"
        CD = "CD","COORDINADOR"
        PR = "PR","PROFESOR"
        SU = "SU","SUPERUSER"

class Usuario(models.Model):
    rol = models.CharField(choices=Roles.choices,default=Roles.NA.name,max_length=2)
    uvus = models.CharField(max_length=10)
    passwordHash = models.IntegerField()

    def __str__(self):
        return self.uvus
