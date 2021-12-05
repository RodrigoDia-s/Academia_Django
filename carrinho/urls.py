from django.urls import path

from .views import cart_add, cart_detail

app_name = "carrinho"

urlpatterns = [
    path("order_form/<int:plano_id>/", cart_add, name="add"),
    path("", cart_detail, name="detail"),
]