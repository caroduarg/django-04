from django.urls import path, include
from .views import *

urlpatterns = [
    path('',PostListView.as_view(), name='post-list'),
    path('post/create/',PostCreate.as_view(), name='post-create'),
    path('post/detail/<int:pk>', PostDetail.as_view(), name='post-detail'),
]