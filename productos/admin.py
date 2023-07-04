from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    # exclude para que no se muestre en el formulario
    exclude = ('creado_en', )
    # list_display para personalizar los campos que queremos visualizar
    list_display = ('id', 'nombre', 'stock', 'puntaje',
                    'categoria', 'creado_en')


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
