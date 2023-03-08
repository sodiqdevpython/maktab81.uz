from django.urls import path
from .views import TeacherInfo, TeacherInfoUpdate, TeacherInfoDelete
from .views import search_teacher
urlpatterns = [
    path('',TeacherInfo.as_view(), name='teacher_info'),
    path('edit/<int:pk>/',TeacherInfoUpdate.as_view(), name='edit_teacher_info'),
    path('remove/teacher/<int:pk>/', TeacherInfoDelete.as_view(), name='remove_teacher_info'),
    path('search_teacher/', search_teacher, name='search_teacher')
]