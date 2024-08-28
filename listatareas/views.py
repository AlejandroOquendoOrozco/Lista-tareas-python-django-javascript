from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from .models import Tarea  # Importa tu modelo Tarea
from django.views.decorators.http import require_http_methods

def index(request: HttpRequest) -> HttpResponse:
    obj_tareas = Tarea.objects.all()  
   
    return render(request, 'GestionTareas.html', {"tareas": obj_tareas})  

@require_http_methods(["POST"])
def registar_curso(request: HttpRequest) -> HttpResponse:

    info_titulo = request.POST.get('txtTitulo')
    info_descripcion = request.POST.get('txtareaDescripcion')
    info_fecha = request.POST.get('date')

    Tarea.objects.create(
        titulo=info_titulo,
        descripcion=info_descripcion,
        fecha=info_fecha
    )
    
    return redirect('/')

    

def eliminar_tarea(request:HttpRequest,codigo:str)->HttpResponse:

    tarea=Tarea.objects.get(codigo=codigo)
    tarea.delete()

    return redirect("/")


