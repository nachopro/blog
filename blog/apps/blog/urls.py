from django.urls import path

from .views import index, post_detail


urlpatterns = [
    path('', index, name='blog-index'),
    path('<slug:slug>/', post_detail, name='blog-post'),
]
