from django.contrib import admin
from inventario.models import Producto
from necesidades.models import Necesidad

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "unidades", "valorMonetario")
    search_fields= ("nombre", "categoria")
    list_filter = ("categoria",)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Necesidad)