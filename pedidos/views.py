from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from carrinho.carrinho import Cart

from .forms import OrderCreateForm
from .models import Item, Order


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm

    def form_valid(self, form):
        cart = Cart(self.request)
        if cart:
            order = form.save()
            for item in cart:
                Item.objects.create(
                    pedido=order,
                    plano=item["plano"],
                    price=item["preco"],
                    quantity=item["quantidade"],
                )
            cart.clear()
            self.request.session["order_id"] = order.id
            return redirect(reverse("payments:process"))
        return redirect(reverse("pages:home"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carrinho"] = Cart(self.request)
        return context
