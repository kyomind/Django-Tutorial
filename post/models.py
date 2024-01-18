from django.db import models


# 文章
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'<{self.id}>: {self.title}'


# 可選的副標題
class Subtitle(models.Model):
    content = models.CharField(max_length=100)
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='subtitle')

    def __str__(self):
        return f'<{self.id}>: {self.content}'


# 留言
class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'<{self.id}>: {self.content}'
