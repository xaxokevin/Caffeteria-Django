from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','author','published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    
    def post_categories(self, obj):
    #define new list_display because categories is not a callable attribute
    #return string with the name of category
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)