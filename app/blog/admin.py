from django.contrib import admin
from .models import Post, Category, Tag, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'pub_date', 'created_on']
    list_editable = ('status',)
    search_fields = ('title',)
    list_filter = ['status', 'created_on']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_on']
    # list_editable = ('title', )
    search_fields = ('title',)
    list_filter = ['title', 'created_on']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    # list_editable = ('name',)
    search_fields = ('name',)
    # list_filter = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'status', 'created_on']
    list_editable = ('status',)
    search_fields = ('name', 'email',)
    list_filter = ['status', 'created_on']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
