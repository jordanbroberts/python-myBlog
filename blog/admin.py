from django.contrib import admin
from blog.models import Post, Category
# Register your models here.
class Admin(admin.ModelAdmin):
	list_filter = ['created_on']
	search_fields = ['title', 'text']
	list_display = ['title','category']

admin.site.register(Post,Admin)
admin.site.register(Category)
