from django.urls import path

from .views import  PlanoListView

app_name = "planos"

urlpatterns = [
    path("plano_list", PlanoListView.as_view(), name="list"),
  
   
]
