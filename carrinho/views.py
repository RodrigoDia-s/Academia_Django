from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from planos.models import Plano

from .carrinho import Cart
from pedidos.models import Order
from .forms import CartAddplanoForm


@require_POST
def cart_add(request, plano_id):
    cart = Cart(request)
    pedidos = Order(request)
    plano = get_object_or_404(Plano, id=plano_id)

    form = CartAddplanoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            plano=plano, quantity=cd["quantity"], override_quantity=cd["override"] # VER NO VIDEO O QUE É OVERRIDE
        )

    return redirect("carrinho:detail") # MUDAR PARA RETORNAR PARA PAGINA DE CHECKOUT


def cart_detail(request):
    cart = Cart(request)
    return render(request, "pedidos/order_form.html", {"cart": cart})