from datetime import datetime
from enum import auto
from operator import mod
from django.db import models

class Post(models.Model):
    id =models.IntegerField(primary_key=True,auto_created=True)
    titulo=models.CharField(max_length=25)
    contenido=models.CharField(max_length=250)
    fecha=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "ID: " + self.id + "TÍTULO: " + self.titulo + "CONTENIDO: " + self.contenido +"FECHA: " + self.fecha

