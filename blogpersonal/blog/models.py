from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen')
    title = models.CharField(max_length=200, verbose_name='Titulo')
    desc = models.TextField(verbose_name='Descripción')
    content = models.TextField(verbose_name='Contenido')
    
    created = models.DateField(
        auto_now_add=True,verbose_name='Fecha de Creación')
    updated = models.DateField(
        auto_now=True, verbose_name='Fecha de Actialización')
    
    class Meta:
        verbose_name = 'Publicaciones'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title 
    