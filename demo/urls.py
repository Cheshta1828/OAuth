
from django.contrib import admin
from django.urls import path, include # added
from django.views.generic import TemplateView # added

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticate/',include('drf_social_oauth2.urls', namespace='drf')),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('users/', include('users.urls')),
]
