from django.db import models

# Create your models here.


class Tarea(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    fecha = models.DateField()


    