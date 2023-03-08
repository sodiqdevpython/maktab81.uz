from django.urls import path

from .views import quistion, qiuz, result_list

urlpatterns = [
    path('', qiuz, name='qiuz'),
    path('quiz/<int:pk>/', quistion, name='quistion'),
    path('results/<int:pk>/', result_list, name='result_detail'),
]