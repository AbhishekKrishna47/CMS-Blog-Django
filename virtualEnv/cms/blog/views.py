from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here

def list_of_posts(request):
    posts = Post.objects.all()
    template = 'blog/post/list_of_post.html'  # Corrected single quotes to standard syntax
    context = {'posts': posts}  # Corrected quotation marks
    return render(request, template, context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)  # Fetching the post using slug
    template = 'blog/post/post_detail.html'  # Corrected single quotes to standard syntax
    context = {'post': post}  # Corrected quotation marks
    return render(request, template, context)
