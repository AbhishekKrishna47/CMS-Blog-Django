from django.contrib import admin
from .models import Post, Category, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'post', 'created', 'approved')  # Display these fields in the admin list view
    list_filter = ('approved', 'created')  # Add filters for approval status and creation date
    search_fields = ('user', 'email', 'body')  # Add search bar for specific fields
    actions = ['approve_comments']  # Add custom action for bulk approval

    def approve_comments(self, request, queryset):
        """Custom admin action to approve selected comments."""
        queryset.update(approved=True)
    approve_comments.short_description = 'Approve selected comments'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Display these fields in the admin list view
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from the name

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'published')  # Fields to display in list view
    list_filter = ('status', 'created', 'published', 'category')  # Filters for sidebar
    search_fields = ('title', 'content')  # Searchable fields
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from the title
    raw_id_fields = ('author',)  # Improves author selection when there are many users
    date_hierarchy = 'published'  # Adds a date hierarchy for filtering by published date
    ordering = ('status', 'published')  # Default ordering
