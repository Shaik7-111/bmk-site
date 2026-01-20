from django.db import models
from django.conf import settings

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('rice', 'Rice'),
        ('pulses', 'Pulses'),
        ('oils', 'Oils'),
        ('spices', 'Spices'),
        ('dryfruits', 'Dry Fruits'),
        ('others', 'Other Groceries'),
    ]

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # 🔥 prevents duplicates

    def __str__(self):
        return f"{self.user} - {self.product.name}"