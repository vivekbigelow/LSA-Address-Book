"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from contacts.views import home_view, contacts_view, contact_create_view,contact_delete_view,contact_edit_view,contact_details_view, register_view, login_view, logout_view,search_view,search_results_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contacts/', contacts_view, name='contacts'),
    path('create/', contact_create_view, name='create'),
    path('contacts/<int:id>/delete/', contact_delete_view, name="delete"),
    path('contacts/<int:id>/edit/', contact_edit_view, name="edit"),
    path('contacts/<int:id>/',contact_details_view, name="contact-details"),
    path('register/',register_view,name='register'),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('search/', search_view,name="search"),
    path('search-results/', search_results_view,name="search-results")
  
]
