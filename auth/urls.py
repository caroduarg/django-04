from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('crear/', views.crear_publicacion, name='publicaciones:crear'),
    path('publicaciones/', views.lista_publicaciones, name='publicaciones:lista'),
    # ... otras URLs
]