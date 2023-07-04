from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto

# Create your views here.


def index(request):
    # return HttpResponse('Hola Mundo!')

    # productos = Producto.objects.all().values()
    # # Esto para retornar en formato Json
    # return JsonResponse(list(productos), safe=False)

    productos = Producto.objects.all()

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    # get object or 404 es una herramienta de django que ahorra el usar el try/catch para ciertos casos, en este mostrar error 404 si el objeto a buscar no existe en la BDD
    producto = get_object_or_404(Producto, id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
