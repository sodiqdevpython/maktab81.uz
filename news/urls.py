from django.urls import path
from .views import NewsView, DetailNewsView
urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('article/<int:pk>/', DetailNewsView.as_view(), name='news_detail')
]