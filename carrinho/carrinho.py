import copy
from decimal import Decimal

from django.conf import settings

from planos.models import Plano

from .forms import CartAddPlanoForm


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
            cart[str(plano.id)]["Plano"] = plano

        for item in cart.values():
            item["preco"] = Decimal(item["preco"])
            item["total_price"] =  item["preco"]
           
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, plano):
        Plano_id = str(plano.id)

        if Plano_id not in self.cart:
            self.cart[Plano_id] = {
                "preco": str(plano.preco)
            }

        

        self.save()

    def remove(self, Plano):
        Plano_id = str(Plano.id)

        if Plano_id in self.cart:
            del self.cart[Plano_id]
            self.save()

    def get_total_price(self):
        return sum(
            Decimal(item["preco"]) * 1 for item in self.cart.values()
        )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
