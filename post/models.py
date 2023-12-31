from django.db import models


# 文章
class Post(models.Model):
    title = models.OneToOneField('Title', on_delete=models.PROTECT, related_name='post')
    content = models.TextField()

    def __str__(self):
        return f'<{self.id}>: {self.title.main} - {self.title.subtitle}'


# 文章標題
class Title(models.Model):
    main = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

    def __str__(self):
        return f'<{self.id}>: {self.main}'


# 留言
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return f'<{self.id}>: {self.content}'
