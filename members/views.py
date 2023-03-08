from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from .forms import SignUpForm, EditProfileForm
from django.urls import reverse_lazy


# Create your views here.


class CreateUser(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
