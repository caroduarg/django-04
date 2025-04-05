from django.urls import path, include
from .views import PostListView
from .views import PostCreate

urlpatterns = [
    path('',PostListView.as_view(), name='post-list'),
    path('create/',PostCreate.as_view(), name='post-create'),
]