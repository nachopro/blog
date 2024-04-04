from django.urls import path

from .views import up


urlpatterns = [
    path('', up, name='healthcheck-up'),
]
