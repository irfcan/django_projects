from django.urls import path
from store import views

urlpatterns = [
    path("", views.StoreView.as_view(), name="store"),
]