from django.urls import path
from .views import home, post_message

urlpatterns = [
    path('', home, name='home'),
    path('post_message/', post_message, name='post_message')
]