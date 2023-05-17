from django.urls import path
from . import views
from post.views import index,detail,category

urlpatterns = [
    path('',views.index,name="index"),

    path('detail/',views.detail,name='detail'),
    path('category/',views.category,name='category')
    
]
