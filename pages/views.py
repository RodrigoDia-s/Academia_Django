from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods    

class HomePageView(TemplateView):
    template_name = "index.html"
    
def cadastroc(request):
    return render(request, "cadastroCliente.html")
