from django.urls import path
from .views import ViewSchool
urlpatterns = [
    path('',ViewSchool.as_view(), name='map')
]