from django.shortcuts import render, redirect
from .models import SchoolData, MoreInformation, SchoolContact, FAQ
from news.models import News
from .forms import AddMessageForm

# Create your views here.
def home(request):
    news = News.objects.order_by('-id')[:3]
    school_data = SchoolData.objects.all()
    data_about = MoreInformation.objects.all()
    contact = SchoolContact.objects.all()[0]
    faq = FAQ.objects.all()
    return render(request, 'home.html', {'school_data': school_data,'data_about': data_about, 'faq': faq, 'contact': contact, 'news': news})

def post_message(request):
    form = AddMessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    return redirect('home')