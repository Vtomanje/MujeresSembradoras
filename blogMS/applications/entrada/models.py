# satandar Library
from datetime import timedelta, datetime
# librerias de django
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
# app de terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import EntryManager


class Category (TimeStampedModel):
    """ Categorias de una entrada """
    
    short_name = models.CharField('Nombre corto', max_length=60, unique=True)
    name = models.CharField('Nombre', max_length=60, unique=True)
    
 
    
    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name
    

class Tag(TimeStampedModel):
    """ etiquetas de articulos"""
    
    name = models.CharField('Nombre', max_length=30)
    
    class Meta():
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'
        
    def __str__(self):
        return self.name
    

class Entry(TimeStampedModel):
    """ Modelo de entradas o articulos"""
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen', blank=True, null=True)
    content = RichTextUploadingField('Contenido', blank=True, null=True)
    publicado = models.DateField('Fecha de Publicacion', blank=True, null=True)
    public = models.BooleanField(default=False)
    image = models.ImageField('Imagen', upload_to='Entry')
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)
    
    objects = EntryManager()
    
    class Meta():
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy(
            "entrada_app:entry-detail", 
            kwargs={"slug": self.slug})
    
    
    def save(self, *args, **kwargs):
        # calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))
        
        self.slug = slugify(slug_unique)
        
        super(Entry, self).save(*args, **kwargs)
        
class Instagram(TimeStampedModel):
    """ Imagenes para Instagram """
    
    name = models.CharField('Nombre', max_length=200)
    public = models.BooleanField(default=False)
    image1 = models.ImageField('Imagen 1', upload_to='Instagram', null=True)
    image2 = models.ImageField('Imagen 2', upload_to='Instagram', null=True)
    image3 = models.ImageField('Imagen 3', upload_to='Instagram', null=True)
    image4 = models.ImageField('Imagen 4', upload_to='Instagram', null=True)
    image5 = models.ImageField('Imagen 5', upload_to='Instagram', null=True)
    image6 = models.ImageField('Imagen 6', upload_to='Instagram', null=True)
    image7 = models.ImageField('Imagen 7', upload_to='Instagram', null=True)
    image8 = models.ImageField('Imagen 8', upload_to='Instagram', null=True)
    image9 = models.ImageField('Imagen 9', upload_to='Instagram', null=True)
   
    
    objects = EntryManager()
    
    class Meta:
        verbose_name = 'Imagen Instagram'
        verbose_name_plural = 'Imagenes Instagram'
        
        def __str__(self):
            return self.name
        
    
    
    
    
        
