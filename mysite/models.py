from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    picture = models.ImageField(upload_to='products/', blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
