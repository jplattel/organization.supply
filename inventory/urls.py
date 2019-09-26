"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from dashboard import views
from dashboard import views_users

urlpatterns = [
    # Inventory urls
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("locations", views.locations, name="locations"),
    path("inventory", views.inventory, name="inventory"),
    path("mutations", views.mutations, name="mutations"),
    path("products", views.products, name="products"),
    # User urls
    path("login", views_users.login, name="users_login"),
    path("logout", views_users.logout, name="users_logout"),
    # Admin
    path("admin/", admin.site.urls),
]
