from django.shortcuts import render
from .models import SchoolData, MoreInformation, SchoolContact
from news.models import News
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    news = News.objects.order_by('-id')[:3]
    school_data = SchoolData.objects.all()
    data_about = MoreInformation.objects.all()
    total_users = User.objects.all().count()
    contact = SchoolContact.objects.all()[0]
    return render(request, 'home.html', {'school_data': school_data,'data_about': data_about, 'total_users': total_users, 'contact': contact, 'news': news})