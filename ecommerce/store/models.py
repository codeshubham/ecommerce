from django.db import models


class Category(models.Model): 
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creater')
    title = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'images/')