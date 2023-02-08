from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('/<int:pk>/detail/', Detail.as_view(), name='detail'),
    path('course/', Course.as_view(), name='course'),
    path('team/', Team.as_view(), name='team'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
    path('feature/', Feature.as_view(), name='feature'),
    
]