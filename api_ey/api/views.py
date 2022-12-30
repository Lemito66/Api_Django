from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Articulos
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


class ManufactureView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            pass
        else:
            manufacture = list(Articulos.objects.values())
            if len(manufacture) > 0:
                data = {'message': "Éxito", 'manufacture': manufacture}
            else:
                data = {'message': "No hay datos"}
            return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Articulos.objects.create(codigo_articulo=jd['codigo_articulo'], nombre_articulo=jd['nombre_articulo'],
                                 descripcion_articulo=jd['descripcion_articulo'], cantidad_disponible_del_articulo=jd['cantidad_disponible_del_articulo'])
        data = {'message': "Éxito"}
        return JsonResponse(data)

    def put(self, request): pass
    def delete(self, request): pass
