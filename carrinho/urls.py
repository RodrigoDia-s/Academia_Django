from django.urls import path

from .views import cart_add

app_name = "carrinho"

urlpatterns = [
    path("add/<int:plano_id>/", cart_add, name="add"),
]