from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('quienes-somos', views.quienesSomosView.as_view(), name='quienes-somos'),  
    path('contacto', views.ContactoView.as_view(), name='contacto'),  
    path('', views.HomePageView.as_view(), name='index'),  
    path('register-suscripcion', views.SuscribersCreateView.as_view(), name='add-suscripcion'),  
    path('contact', views.contacto, name='add-contact'),   
]