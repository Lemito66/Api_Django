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
            manufacture = list(Articulos.objects.filter(id=id).values())
            if len(manufacture) > 0:
                manufactures = manufacture[0]
                data = {'message': "Éxito", 'manufacture': manufactures}
            else:
                data = {'message': "No Funciona"}
            return JsonResponse(data)
        else:
            manufacture = list(Articulos.objects.values())
            if len(manufacture) > 0:
                data = {'message': "Éxito", 'manufacture': manufacture}
            else:
                data = {'message': "No funciona"}
            return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        convert_data_in_json = json.loads(request.body)
        # print(convert_data_in_json)
        Articulos.objects.create(codigo_articulo=convert_data_in_json['codigo_articulo'], nombre_articulo=convert_data_in_json['nombre_articulo'],
                                 descripcion_articulo=convert_data_in_json['descripcion_articulo'], cantidad_disponible_del_articulo=convert_data_in_json['cantidad_disponible_del_articulo'])
        data = {'message': "Éxito"}
        return JsonResponse(data)

    def put(self, request, id):
        convert_data_in_json = json.loads(request.body)
        manufacture = list(Articulos.objects.filter(id=id).values())
        if len(manufacture) > 0:
            article = Articulos.objects.get(id=id)
            article.codigo_articulo = convert_data_in_json['codigo_articulo']
            article.nombre_articulo = convert_data_in_json['nombre_articulo']
            article.descripcion_articulo = convert_data_in_json['descripcion_articulo']
            article.cantidad_disponible_del_articulo = convert_data_in_json[
                'cantidad_disponible_del_articulo']
            article.save()
            data = {'message': "Éxito"}
        else:
            data = {'message': "No funciona"}
        return JsonResponse(data)
    
    def delete(self, request, id):
        manufacture = list(Articulos.objects.filter(id=id).values())
        if len(manufacture) > 0:
            Articulos.objects.get(id=id).delete()
            data = {'message': "Éxito"}
        else:
            data = {'message': "No funciona"}
        return JsonResponse(data)
