from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post,Category

# Create your views here.
def index(request):
    posts=Post.objects.all()
    categories=Category.objects.all()
    context={
        'posts':posts,
        'categories': categories
    }
    return render(request,"post/index.html",context)

def detail(request):
    return render(request,"post/detail.html")
def category(request):
    categories=Category.objects.all()
    context={
        'categories': categories
    }
    return render(request,"post/category.html")