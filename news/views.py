from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
# Create your views here.

class NewsView(ListView):
    model = News
    template_name = 'news.html'
    ordering = ['-id']
    paginate_by = 3

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class DetailNewsView(DetailView):
    model = News
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailNewsView,self).get_context_data(*args, **kwargs)
        return context