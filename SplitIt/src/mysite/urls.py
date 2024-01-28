"""
URL configuration for mysite project.

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
from django.urls import path

from personal.views import home_screen_view
from personal.views import payment_screen_view
from account.views import registration_view
from account.views import logout_view
from account.views import login_view
from split.views import form_checkbox

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('payments', payment_screen_view, name='payment'),
    path('register', registration_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('login', login_view, name='login'),
    path('split', form_checkbox, name='split')
]
