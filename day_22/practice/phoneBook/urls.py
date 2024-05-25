from django.urls import path
from phoneBook import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("phone-create/", views.PhoneCreateView.as_view(), name="phone_create"),
    path("phone-list/", views.PhoneListView.as_view(), name="phone-list"),
    path("category-create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("<slug:slug>/", views.PhoneDetailView.as_view(), name="phone-detail"),
    path("phone-edit/<slug:slug>/", views.PhoneEditView.as_view(), name="phone-edit"),
    path("phone-delete/<slug:slug>/", views.PhoneDeleteView.as_view(), name="phone-delete"),
    path("category/<slug:slug>/", views.CategoryPhoneListView.as_view(), name="phone-by-category"),
]