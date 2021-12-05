import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


def test_reverse_resolve():
    assert reverse("pedidos:create") == "/pedidos/create/"
    assert resolve("/pedidos/create/").view_name == "pedidos:create"


def test_status_code(client):
    response = client.get(reverse("pedidos:create"))
    assert response.status_code == 200


def test_order_create_form_valid(order_form_data, client, plano):
    response = client.post(reverse("pedidos:create"), data=order_form_data, follow=True)
    assertTemplateUsed(response, "home.html")

    client.post(
        reverse("cart:add", kwargs={"plano_id": plano.id}),
        data={"quantity": 1, "override": False},
    )

    response = client.post(reverse("pedidos:create"), order_form_data, follow=True)
    assertTemplateUsed(response, "payments/payment_form.html")
