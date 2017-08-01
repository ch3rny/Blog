from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author','created_time','theme','text','unread')
    date_hierarchy = 'created_time'

admin.site.register(Review, ReviewAdmin)