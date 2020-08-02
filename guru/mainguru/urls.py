from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
]