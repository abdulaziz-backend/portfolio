from django.contrib import admin
from django.urls import path
from . import views
from .views import contact_view, contact_success_view

urlpatterns = [
    path('', views.about),
    path('about', views.about),
    path('portfolio', views.port),
    path('contact', views.contact),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
]