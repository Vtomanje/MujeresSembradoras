from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Entry, Category, Instagram


class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name= 'entradas' # el: context_object_name= es para acceder en ese contexto por el html
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        
        return context
    
    
    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria", '') 
        # Consulta de busqueda
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado
    
class EntryDetailView(DetailView):
    template_name = "entrada/detail.html"
    model = Entry
    
    def get_context_data(self, *args, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        
        # contexto para los articulos en instagram
        context["instagram"] = Instagram.objects.latest('created')
        
        return context
    
    

