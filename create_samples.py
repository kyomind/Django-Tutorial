import os

import django

# 設定環境變數
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoTutorial.settings")

# 初始化 Django
django.setup()


from post.models import Comment, Post, Title


def create_samples():
    # 建立Title資料
    title1 = Title.objects.create(main="數位斷捨離", subtitle="AI時代的生存指南")
    title2 = Title.objects.create(main="精通python讀後感", subtitle="Python程式設計的學習心得")
    title3 = Title.objects.create(main="如何使用 Poetry", subtitle="簡化Python專案管理的工具介紹")

    # 建立Post資料
    post1 = Post.objects.create(title=title1, content="數位斷捨離帶給我新的生活觀")
    post2 = Post.objects.create(title=title2, content="Python的豐富功能讓我愛不釋手")
    Post.objects.create(title=title3, content="Poetry使得Python專案管理變得輕鬆自在")

    # 建立Comment資料
    Comment.objects.create(post=post1, content="實用的心得分享")
    Comment.objects.create(post=post1, content="喜歡這篇文章")
    Comment.objects.create(post=post2, content="確實是好書")

    print("建立範例資料完成")


if __name__ == "__main__":
    create_samples()
