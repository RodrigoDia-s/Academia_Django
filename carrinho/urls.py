from django.urls import path

from .views import cart_add, cart_detail

app_name = "cart"

urlpatterns = [
    path("", cart_detail, name="detail"),
    path("/<int:plano_id>/", cart_add, name="add"),
]