from django.urls import path

from post.views import hello_world

urlpatterns = [
    path('hello/', hello_world),
]
