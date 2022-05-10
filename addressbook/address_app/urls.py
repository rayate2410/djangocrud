"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.address_list), name='address_list'),
    path('new/', login_required(views.AddressCreateView.as_view()), name='address_create'),
    path('<int:pk>/edit', login_required(views.AddressUpdateView.as_view()), name='address_edit'),
    path('<int:pk>/delete', login_required(views.AddressDeleteView.as_view()), name='address_delete')
]
