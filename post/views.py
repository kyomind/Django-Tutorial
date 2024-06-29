from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from post.models import Post


def hello_world(request):
    return JsonResponse({'message': 'Hello, world!'})


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
