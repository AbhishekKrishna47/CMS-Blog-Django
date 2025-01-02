from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_posts, name='list_of_posts'),  # Root path
    path('posts/', views.list_of_posts, name='list_of_posts'),  # Posts listing
    path('create/', views.create_post, name='create_post'),  # Post creation
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Post details
    path('category/<slug:category_slug>/', views.list_of_posts_by_category, name='list_of_posts_by_category'),  # Posts by category
]
