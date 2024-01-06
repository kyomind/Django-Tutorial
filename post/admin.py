from django.contrib import admin

from post.models import Comment, Post, Subtitle

admin.site.register(Post)
admin.site.register(Subtitle)
admin.site.register(Comment)
