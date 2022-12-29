from django.contrib import admin
from . import views
from django.urls import re_path
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('login.rutas')),
    path('core/index', views.index),
    path('core/historia', views.historia),
    path('core/reservar', views.reservar),
    path('core/reservas', views.reservas),
    path('core/eliminar', views.eliminar),
    path('core/terminar_reserva', views.terminar_reserva),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # para que se vean los archivos de media
