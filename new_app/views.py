from django.shortcuts import render
from .models import SchoolData, TopWorkers,MainSlider, MoreInformation
# Create your views here.
def home(request):
    worker = TopWorkers.objects.all()
    school_data = SchoolData.objects.all()
    main_slider = MainSlider.objects.all()
    data_about = MoreInformation.objects.all()
    return render(request, 'home.html', {'worker': worker, 'school_data': school_data, 'main_slider': main_slider, 'data_about': data_about})