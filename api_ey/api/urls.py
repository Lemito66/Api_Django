from django.urls import path
from .views import ManufactureView
urlpatterns = [
    path('articulos/', ManufactureView.as_view(), name='articulo'),
    path('articulos/<int:id>', ManufactureView.as_view(), name='articulo_con_procesos'),
    
]
