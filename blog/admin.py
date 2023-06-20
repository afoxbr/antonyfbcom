from django.contrib import admin

from .models import Tag, Post, Image


admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Image)
