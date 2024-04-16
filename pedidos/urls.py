from django.urls import path

from .views import OrderCreateView

app_name = "pedidos"

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="create"),
       path("detail", OrderCreateView.as_view(), name="detail"),
]
