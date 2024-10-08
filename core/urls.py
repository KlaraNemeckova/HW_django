from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('core/', views.core, name='core'),
    path('core_new/', views.core_new, name='core_new'),
]