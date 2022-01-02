from django.contrib import admin
from . import models

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("uvus","rol")
    list_editable = ["rol"]

admin.site.register(models.Usuario,UsuarioAdmin)