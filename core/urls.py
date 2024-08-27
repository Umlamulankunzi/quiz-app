"""
URL configuration for core pages of quiz-wiz project.

"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/info/', views.api_info, name='api_info'),
    path('api/terms-of-use/', views.api_terms_of_use, name='api_terms_of_use'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
