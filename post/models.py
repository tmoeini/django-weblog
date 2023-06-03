from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)    
    available=models.BooleanField(default=True)
    created=models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="گروه"
        verbose_name_plural="گروه ها"
    

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_posts")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="cat_posts")
    
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)
    body=models.TextField()
    banner=models.ImageField(blank=True,null=True,upload_to="posts/%y/%m/%d")
    created_date=models.DateTimeField(auto_now=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    published=models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="پست"
        verbose_name_plural="پست ها"
    
        
    

    
    
    
    

