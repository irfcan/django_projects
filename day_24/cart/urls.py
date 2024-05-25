from django.urls import path
from cart import views

urlpatterns = [
    path("", views.CartSummaryView.as_view(), name="cart_summary"),
    path("add/", views.CartAddView.as_view(), name="cart_add"),
    path("delete/", views.CartDeleteView.as_view(), name="cart_delete"),
    path("update/", views.CartUpdateView.as_view(), name="cart_update"),
]