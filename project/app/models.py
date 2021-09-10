from django.db import models

# Create your models here.


class Category(models.Model):
    title     = models.CharField(max_length=255, null=False, blank=False)
    active 	  = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated   = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-timestamp',)
        
        
class Post(models.Model):
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    title     = models.CharField(max_length=255, null=False, blank=False)
    content   = models.TextField(null=False, blank=False)
    active 	  = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated   = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-timestamp',)
