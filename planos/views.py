from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, ListView
from carrinho.forms import CartAddplanoForm

from .models import Plano


class PlanoDetailView(DetailView):
    queryset = Plano.objects.all()
    extra_context = {"form": CartAddProductForm()}