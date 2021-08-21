from django.shortcuts import render

from blog_main.models import Post

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')
