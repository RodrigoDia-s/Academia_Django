import copy
from decimal import Decimal

from django.conf import settings

from planos.models import Plano

from .forms import CartAddplanoForm


class Cart:
    def __init__(self, request):
        if request.session.get(settings.CART_SESSION_ID) is None:
            request.session[settings.CART_SESSION_ID] = {}

        self.cart = request.session[settings.CART_SESSION_ID]
        self.session = request.session

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        planos = Plano.objects.filter(id__in=cart)
        for plano in planos:
            cart[str(plano.id)]["plano"] = plano

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["quantity"] * item["price"]
            item["update_quantity_form"] = CartAddplanoForm(
                initial={"quantity": item["quantity"], "override": True}
            )

            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, plano, quantity=1, override_quantity=False):
        plano_id = str(plano.id)

        if plano_id not in self.cart:
            self.cart[plano_id] = {
                "quantity": 0,
                "price": str(plano.price),
            }

        if override_quantity:
            self.cart[plano_id]["quantity"] = quantity
        else:
            self.cart[plano_id]["quantity"] += quantity

        self.cart[plano_id]["quantity"] = min(20, self.cart[plano_id]["quantity"])

        self.save()

    def remove(self, plano):
        plano_id = str(plano.id)

        if plano_id in self.cart:
            del self.cart[plano_id]
            self.save()

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
