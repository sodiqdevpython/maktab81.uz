from django.urls import path
from .views import ViewSchool, SchoolStaffsView, AbilityPupilsView
urlpatterns = [
    path('',ViewSchool.as_view(), name='map'),
    path('xodimlar/',SchoolStaffsView.as_view(), name='staffs'),
    path('iqtidorli/',AbilityPupilsView.as_view(), name='pupils'),
]