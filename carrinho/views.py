from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from planos.models import Plano

from .carrinho import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, plano_id):
    cart = Cart(request)
    plano = get_object_or_404(Plano, id=plano_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            plano=plano, quantity=cd["quantity"], override_quantity=cd["override"] # VER NO VIDEO O QUE É OVERRIDE
        )

    return redirect("cart:detail") # MUDAR PARA RETORNAR PARA PAGINA DE CHECKOUT