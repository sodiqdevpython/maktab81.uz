from django.shortcuts import render
from .models import SchoolData, TopWorkers
# Create your views here.
def home(request):
    worker = TopWorkers.objects.all()
    school_data = SchoolData.objects.all()
    return render(request, 'home.html', {'worker': worker, 'school_data': school_data})