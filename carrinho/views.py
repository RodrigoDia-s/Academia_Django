from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from planos.models import Plano 

from .carrinho import Cart
from .forms import CartAddPlanoForm


@require_POST
def cart_add(request, plano_id):
    cart = Cart(request)
    plano = get_object_or_404(Plano, id=plano_id)

    
    cart.add(
        plano=plano
    )

    return redirect("cart:detail")


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Plano, id=product_id)
    cart.remove(product)
    return redirect("cart:detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "planos/plano_detail.html", {"cart": cart})
