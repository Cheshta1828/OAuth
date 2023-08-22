"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path, include # added
from django.views.generic import TemplateView # added
from .views import CustomUserCreate, LoginView # added
from . import views
from django.urls import path, re_path




urlpatterns = [
    path('register/', CustomUserCreate.as_view()),
    path('login/', LoginView.as_view()),
    #re_path('api/register-by-access-token/' + r'social/(?P<backend>[^/]+)/$', views.register_by_access_token),
    #path('api/authentication-test/', views.authentication_test),
    
   
]
