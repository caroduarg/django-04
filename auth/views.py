from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignUpView (CreateView):
    template_name = 'authentication/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list')