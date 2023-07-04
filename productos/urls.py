from django.urls import path
from . import views

# Convención que sigue django a la hora de moverse entre rutas, si exuisten dos urls con el mismo nombre puede generar conflicto y enviar donde no queremos, por esto
# se usa el nombre de la app antes del nombre, pero django usa el app_name para evitar nosotros tener que escribirlo manualmente, lo que hace django es concadenar
# el nombre de al app_name al nombre de nuestras urls
app_name = 'productos'

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('<int:producto_id>', views.detalle, name='detalle')
]
