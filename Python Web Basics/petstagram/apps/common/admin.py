from django.contrib import admin

from .models import Comment, Like

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (

    )