from django.urls import path
from .views import index

urlpatterns = [
    path("index/", index),
    path("", index),
]


# localhost:8000/blog/index