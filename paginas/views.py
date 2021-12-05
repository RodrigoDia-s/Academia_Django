from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods

from planos.models import Plano    

class HomePageView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['plano_list'] = Plano.objects.all()
        return context
    
    
def cadastroc(request):
    return render(request, "cadastroCliente.html")

def quemSomos(request):
    return render(request, "quemSomos.html")
