from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('up/', include('healthcheck.urls')),
    path('', include('blog.urls')),
]
