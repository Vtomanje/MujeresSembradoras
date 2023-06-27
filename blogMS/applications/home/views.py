import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (TemplateView, CreateView)
from applications.entrada.models import Entry
from .models import Home
from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # carga del texto en home quienes somos
        context["home"] = Home.objects.latest('created')
        # contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # contexto para las entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # enviando formulario de suscripcion
       
        
        context["form"] = SuscribersForm
        
        return context
    

class SuscribersCreateView(CreateView):
   form_class = SuscribersForm
   success_url = '.'
   

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'

    
