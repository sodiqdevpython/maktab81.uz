from django.shortcuts import render
from .models import SchoolMap, SchoolStaffs,AbilityPupils
from django.views.generic import ListView
# Create your views here.

class ViewSchool(ListView):
    model = SchoolMap
    template_name = 'shool_map.html'

class SchoolStaffsView(ListView):
    model = SchoolStaffs
    template_name = 'staffs.html'

class AbilityPupilsView(ListView):
    model = AbilityPupils
    template_name = 'ability_pupils.html'