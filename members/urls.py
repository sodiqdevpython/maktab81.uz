from django.urls import path
from .views import CreateUser, UserEditView
urlpatterns = [
    path('', CreateUser.as_view(), name='signup'),
    path('profile/',UserEditView.as_view(), name='profile')
]