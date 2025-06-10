from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_count', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Number of Products'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'image_preview', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock_quantity')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'stock_quantity', 'image', 'supabase_image_url', 'image_preview', 'category')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.supabase_image_url:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.supabase_image_url)
        elif obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
