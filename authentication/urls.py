from django.urls import path
from .views import *

urlpatterns = [
    path('', HelloWorld, name='hello-world-test'),
]