from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_posts, name='list_of_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Using slug in URL
]
