from django.urls import path
from store import views

urlpatterns = [
    path("", views.StoreGenericView.as_view(), name="store"),
    path("categories/", views.CategoriesGenericView.as_view(), name="categories"),
    path("search/<slug:category_slug>/", views.ListCategoryGenericView.as_view(), name="list-category"),
    path("product/<slug:product_slug>/", views.ProductInfoGenericView.as_view(), name="product-info"),
]