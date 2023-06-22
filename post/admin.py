from django.contrib import admin

from post.models import Comment, Post, Title

admin.site.register(Post)
admin.site.register(Title)
admin.site.register(Comment)
