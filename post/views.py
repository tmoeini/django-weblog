from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def index(request):
    return render(request,"post/index.html")

def detail(request):
    return render(request,"post/detail.html")
def category(request):
    return render(request,"post/category.html")