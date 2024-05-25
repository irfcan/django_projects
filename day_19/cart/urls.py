from django.urls import path
from cart import views

urlpatterns = [
    path("", views.CartSummaryView.as_view(), name="cart-summary"),
]