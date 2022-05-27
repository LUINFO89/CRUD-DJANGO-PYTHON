from ast import Delete
from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.


class Libros (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    descripcion = models.TextField(verbose_name="Descripcion",null=True)


    def __str__(self) :
        fila = "Titulo:" + self.titulo + " - " + "Descripcion:" + self.descripcion
        return fila
    
    def delete(self,using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()