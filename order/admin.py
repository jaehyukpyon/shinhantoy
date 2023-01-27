from django.contrib import admin
from .models import Order, Comment, Like

# Register your models here.

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    pass   

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
