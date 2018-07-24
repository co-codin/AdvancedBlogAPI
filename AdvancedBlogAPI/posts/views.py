from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_create(request):
    pass

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'obj': instance
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'index.html', context)

def post_update(request):
    pass

def post_delete(request):
    pass
