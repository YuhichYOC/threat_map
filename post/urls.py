from django.urls import path

from . import views

urlpatterns = [
    path('new_threat_view/', views.new_threat_view, name='new_threat_view'),
    path('post_new_threat/', views.post_new_threat, name='post_new_threat'),
    path('add_threat_view/', views.add_threat_view, name='add_threat_view'),
    path('post_add_threat/', views.post_add_threat, name='post_add_threat'),
    path('add_peer_review_view/', views.add_peer_review_view, name='add_peer_review_view'),
    path('post_add_peer_review/', views.post_add_peer_review, name='post_add_peer_review'),
]
