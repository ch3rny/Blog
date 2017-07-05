from django.contrib import admin
from .models import Post, Category, UserProfile, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("created_date", "author", "sourse", "text")
    date_hierarchy = 'created_date'

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment, CommentAdmin)