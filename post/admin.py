from django.contrib import admin
from .models import Post,Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','created_date','author','category')
    list_filter=('author','category')
    search_fields=('title',)
    prepopulated_fields={'slug':('title',)}
    ordering=('created_date',)

class CategoryAdmin(admin.ModelAdmin)   :
    list_display=('name','created','available')
    list_filter=('name',)
    search_fields=('name',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
