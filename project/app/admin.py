from django.contrib import admin
from .models import *
# Register your models here.



# SERVICE ADMIN
class PostAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display 		= ['category', 'title', 'active', 'timestamp', 'updated']
    list_display_links 	= ['title']
    list_filter 		= ['title', 'timestamp', 'updated']
    search_fields 		= ['title', 'timestamp', 'updated']
    readonly_fields		= ['timestamp', 'updated']
    list_per_page 		= 25
    class Meta:
        model = Category
admin.site.register(Post, PostAdmin)


admin.site.register(Category)
