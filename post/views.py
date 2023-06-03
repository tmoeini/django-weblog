from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,"post/index.html",context)

def detail(request):
    return render(request,"post/detail.html")
def category(request):
    return render(request,"post/category.html")