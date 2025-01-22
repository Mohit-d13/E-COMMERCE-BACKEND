from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
    
    class Meta:
        ordering = ('name',)
#to get the item in correct spelling order by there name
        verbose_name_plural = 'Categories'
# This is to correct the categorys name in admin with proper spelling 
    def __str__(self):
        return self.name
# This function is to overide the category object default name to name representation

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    #upload_to create a folder to upload a image if it not already created
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)
    #define a one to many relationship from user to item
    created_at = models.DateTimeField(auto_now_add=True)
    #django will automatically add date and time when item is created 

    def __str__(self):
        return self.name