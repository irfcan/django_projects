from django.urls import path
from payment import views

urlpatterns = [
    path("checkout", views.CheckoutView.as_view(), name="checkout"),
    path("complete-order", views.CompleteOrderView.as_view(), name="complete-order"),
    path("payment-success", views.PaymentSuccessView.as_view(), name="payment-success"),
    path("payment-failed", views.PaymentFailedView.as_view(), name="payment-failed"),
]