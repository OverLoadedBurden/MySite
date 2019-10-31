from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Post
import django.core as c


# Create your views here.
def get(request, id: int):
    return HttpResponse(Post.objects.get(['id', id]))

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_id(request, pk):
    print(request)
    w =WSGIRequest()
    w.method
    json = (Post.objects.get(['id', pk]))
    return HttpResponse(json)

