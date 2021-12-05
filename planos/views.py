from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, ListView


from .models import Plano


class PlanoListView(generic.ListView):
    model = Plano
    paginate_by = 6
    queryset = planos = Plano.objects.all()
   
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PlanoListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context