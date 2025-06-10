from django.db import models
from services.storage_service import SupabaseStorageService

class Category(models.Model):
    """Model representing product categories."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

class Product(models.Model):
    """Model representing products in the system."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    supabase_image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Upload image to Supabase if image is set and supabase_image_url is empty or image changed
        if self.image and (not self.supabase_image_url or not self.pk):
            storage_service = SupabaseStorageService()
            upload_result = storage_service.upload_file(self.image, folder='products')
            if upload_result.get('success'):
                self.supabase_image_url = upload_result.get('public_url')
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
            models.Index(fields=['created_at']),
        ]
