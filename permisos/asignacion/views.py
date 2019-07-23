from django.shortcuts import render, redirect
from asignacion.forms import MarcaCampForm,AcountForm
from asignacion.models import Marcaaccount
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'materialize/index.html')


class UploadFileView(CreateView):
    model = Marcaaccount
    form_class = MarcaCampForm
    success_url =  reverse_lazy('index')
    template_name = 'Permisos/asignacionCuenta.html'

#Vista para la pantalla de asginacion de Marca,     
def mascota_view(request):
    #Se pregunta si es un metodo post
    if request.method == 'POST':
        form = MarcaCampForm(request.POST)
        #El idmarca como es foraneo se tiene que tomar del request, de lo contrario lo toma como no valido.
        unit_id = request.POST.get('idmarca')
        form.fields['idmarca'].choices = [(unit_id, unit_id)]
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = MarcaCampForm()

    return render(request, 'Permisos/asignacionCuenta.html', {'form': form})

