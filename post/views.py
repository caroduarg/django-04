from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'
    
class PostCreate(CreateView):
    template_name = 'post_create.html'
    model = Post
    fields = ['title', 'description', 'image', 'author']
    success_url = reverse_lazy('post-list')