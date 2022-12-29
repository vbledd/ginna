from django.contrib import admin
from . import views
from . import costumers
from django.urls import re_path
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin', admin.site.urls),
    #path('', views.index, name='index'),
    path('', include('login.rutas')),
    #path('operador', include('operador.rutas')),
    #path('solicitante', include('solicitante.rutas')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # para que se vean los archivos de media
