from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField("Product name", max_length=255)
    description = models.CharField("Description", max_length=500)
    category = models.CharField("Category", max_length=50)
    created_at = models.DateField("Created_at")
