from django.urls import path

from . import views



urlpatterns=[

    path("",views.index,name="index"),
    path("registrarCurso/",views.registar_curso),
    path("EliminarTarea/<codigo>",views.eliminar_tarea),
  
]