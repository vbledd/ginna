from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='login'),
    path('check_login', views.check_login, name='check_login'),
    path('logout', views.logout, name='logout'),
    path('seleccion', views.seleccion, name='seleccion'),
    path('seleccion_data', views.seleccion_data),
    path('guardar_seleccion', views.guardar_seleccion, name='guardar_seleccion'),
    path('registrar', views.registrar, name='registrar'),
    ]