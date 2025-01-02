from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)  # Unique slug for categories

    class Meta:
        ordering = ['name']  # Order categories alphabetically by name
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Auto-generate slug from name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)  # Unique slug for posts
    content = models.TextField()
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)  # Add category field
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Auto-generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Link comment to a post
    user = models.CharField(max_length=250)  # Name of the user
    email = models.EmailField()  # Email of the user
    body = models.TextField()  # Content of the comment
    created = models.DateTimeField(auto_now_add=True)  # Timestamp of comment creation
    approved = models.BooleanField(default=False)  # Approval status of the comment

    def approve(self):
        """Approve the comment."""
        self.approved = True
        self.save()

    def __str__(self):
        """String representation of the comment."""
        return f"Comment by {self.user} on {self.post.title}"