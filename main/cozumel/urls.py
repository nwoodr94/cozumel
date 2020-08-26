from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('itinerary/', views.itinerary, name="itinerary"),
    path('gallery/', views.gallery, name="gallery"),
    path('reservations/', views.reservations, name="reservations"),
    path('test/', views.test, name="test"),
]




               