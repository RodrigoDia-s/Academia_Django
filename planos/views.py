from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, ListView


from .models import Plano


class PlanoListView(DetailView):
    queryset = Plano.objects.all()
    