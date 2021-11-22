from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('detalhe',views.detalhe, name='detalhe'),
    path('resultados',views.resultados, name='resultados'),
    path('voto',views.voto, name='voto'),
]


