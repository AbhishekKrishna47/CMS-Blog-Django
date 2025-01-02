from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from django.core.paginator import Paginator
from .forms import PostForm

def list_of_posts_by_category(request, category_slug):
    categories = Category.objects.all()  # Retrieve all categories
    category = get_object_or_404(Category, slug=category_slug)  # Get the category by slug
    posts = Post.objects.filter(status='published', category=category)  # Filter posts by category and status

    template = 'blog/post/list_of_post.html'  # Reuse the same template for consistency
    context = {
        'categories': categories,  # Include all categories
        'category': category,  # Current category
        'posts': posts,  # Posts filtered by category
    }
    return render(request, template, context)


def list_of_posts(request):
    categories = Category.objects.all()  # Retrieve all categories
    post_list = Post.objects.filter(status='published')  # Retrieve published posts
    paginator = Paginator(post_list, 5)  # Show 5 posts per page

    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Retrieve the posts for the current page

    context = {
        'categories': categories,
        'page_obj': page_obj,  # Pass the paginated posts to the template
    }
    return render(request, 'blog/post/list_of_post.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)  # Fetch only approved comments
    if request.method == 'POST':
        # Example for handling new comments (form not included here)
        user = request.POST.get('user')
        email = request.POST.get('email')
        body = request.POST.get('body')
        Comment.objects.create(post=post, user=user, email=email, body=body)

    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post/post_detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to create a new post
            return redirect('list_of_posts')  # Redirect to the list of posts
    else:
        form = PostForm()

    return render(request, 'blog/post/create_post.html', {'form': form})