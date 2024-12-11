from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(
        max_length=255,
    )
    text = models.CharField(
        max_length=1000,
    )
    description = models.TextField(null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
def __str__(self):
        return self.title