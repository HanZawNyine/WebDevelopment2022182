from django.shortcuts import render,get_object_or_404
from .models import BlogPost

def post_list(request):
    posts = BlogPost.published.all()
    return render(request,'accounts/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(BlogPost, slug=post,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)
    return render(request,    'accounts/post/detail.html',    {'post': post})