from django.contrib import admin
from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "modified_time"]
    ordering = ("status",)

admin.site.register(Post, PostAdmin)