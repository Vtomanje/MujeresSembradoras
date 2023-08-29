import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import (TemplateView, CreateView)
from applications.entrada.models import Entry
from .models import Home, Contact
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
   

def contacto(request):
    
    if request.method == "POST":
        print(1)
        subject = request.POST["full_name"]
        email = request.POST["email"]
        message = request.POST["messagge"]
        email_from = settings.EMAIL_HOST_USER
        print(2)
        recipient_list = ["mujeressembradorasvidanueva@outlook.com"]
        print(3)
        fulldata = "asunto:" + subject + "\nemail: " + email + "\nmessagge: " + message 

        Contact.objects.create(
            asunto = subject,
            email = email,
            message = message
        )
        print(4)
        send_mail("Correo Recibido desde www.MujeresSembradorasInternacional.com", fulldata, email_from, recipient_list)
       
        return render(request, "contact.html") 
    else:
        return redirect("home_app:index")
        

    
class quienesSomosView(TemplateView):
    template_name = "home/quienes-somos.html"
    
    

    
