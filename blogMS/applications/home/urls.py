from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),  
    path('register-suscripcion', views.SuscribersCreateView.as_view(), name='add-suscripcion'),  
    path('contact', views.ContactCreateView.as_view(), name='add-contact'),  
]