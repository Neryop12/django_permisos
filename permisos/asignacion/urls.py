from asignacion.views import  UploadFileView, index, mascota_view
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^cambio$', mascota_view, name='cambio'),
    
   ]