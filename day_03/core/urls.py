"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls")), # http://localhost:8000/
    # path("users/", include("users.urls")),
    # path("books/", include("books.urls")),
]

# http://localhost:8000/ ==> books app inin altındaki urls.py ye yönlendir
# http://127.0.0.1:8000/ ==> books app inin altındaki urls.py ye yönlendir

# http://localhost:8000/books/ ==> books app inin altındaki urls.py ye yönlendir