from django.urls import path
from .views import *

urlpatterns=[
    path('api', ApiView.as_view(), name='api'),
]