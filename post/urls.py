from django.urls import path

from post import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('posts/', views.get_posts),
]
