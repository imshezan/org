from django.contrib import admin

# Register your models here.
from .models import Post, Category, Gallery


# My Customizations

class PostAdmin(admin.ModelAdmin):
    list_filter = ['updated', 'title']
    search_fields = ['title', 'description']
    list_display = ['title', 'category']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Gallery, PostAdmin)
