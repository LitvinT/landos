from django.contrib import admin


from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    search_fields = ('name', )
    list_filter = ('is_published', )
    ordering = ('is_published', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('name', )
    ordering = ('is_published', 'name')
