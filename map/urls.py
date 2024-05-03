from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_gmap_js/', views.get_gmap_js, name='get_gmap_js'),
]
