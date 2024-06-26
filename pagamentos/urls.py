from django.urls import path

from .views import (
    PaymentCreateView,
    PaymentFailureView,
    PaymentPendingView,
    PaymentSuccessView,
    payment_webhook,
)

app_name = "pagamentos"

urlpatterns = [
    path("process/", PaymentCreateView.as_view(), name="process"),
    path("failure/", PaymentFailureView.as_view(), name="failure"),
    path("pending/", PaymentPendingView.as_view(), name="pending"),
    path("success/", PaymentSuccessView.as_view(), name="success"),
    path("webhook/", payment_webhook, name="webhook"),
]
