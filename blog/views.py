from django.shortcuts import render
from .models import Post, Tag

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def blog(request):
    blogposts = Post.objects.order_by('-date_added')
    context = {'blogposts':blogposts}
    return render(request, 'blog/bloglist.html', context)

def post(request, post_id):
    blogpost = Post.objects.get(id=post_id)
    context = {'blogpost':blogpost}
    return render(request, 'blog/blogpost.html', context)
