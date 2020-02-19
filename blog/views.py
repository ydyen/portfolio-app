from django.shortcuts import render, get_object_or_404
from .models import Blog

def index(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blog})


def details(request, blog_id):
    #returns the blog object model id
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'detail_blogs': detail_blog})