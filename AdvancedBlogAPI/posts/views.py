from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Sucessfully created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not sucessfully created')
    context = {
        'form': form
    }
    return render(request, 'post_form.html', context)


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

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Sucessfully updated')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not sucessfully updated')
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }

    return render(request, "post_form.html", context)

def post_delete(request):
    pass
