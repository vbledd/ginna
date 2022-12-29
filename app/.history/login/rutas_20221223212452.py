from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='login'),
    path('check_login', views.check_login, name='check_login'),
    path('logout', views.logout, name='logout'),
    path('registrar', views.registrar),
    path('registrar/nuevo', views.registrar_nuevo)
    ]