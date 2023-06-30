from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View
from .models import Favorites
from applications.entrada.models import Entry


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('user_app:user-login')
    
    def get_queryset(self):
        return Favorites.objects.entradas_user (self.request.user)
    
class AddFavoritosView(LoginRequiredMixin, View):
    login_url = reverse_lazy('user_app:user-login')
    
    def post(self, request, *args, **kwargs):
        # Recuperar Usuario
        usuario =self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        # Registramos favoritos
        Favorites.objects.create(
            user=usuario,
            entry=entrada,
        )
        
        return HttpResponseRedirect(
            reverse('favoritos_app:perfil')
        )
