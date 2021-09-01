from django.shortcuts import render
from django.urls import reverse_lazy#reverse_lazy is used to send users to particular page wehn they are logged in or out
from . import forms
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')#once signup returns to login page
    template_name = 'accounts/signup.html'
