from django.contrib import admin
from django.urls import path, include  # Use `include` to include app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),  # Include the blog app's URL patterns
]
