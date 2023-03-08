from django.shortcuts import render
from .models import SchoolMap
from django.views.generic import ListView
# Create your views here.

class ViewSchool(ListView):
    model = SchoolMap
    template_name = 'shool_map.html'