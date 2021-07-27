from django.db import models
from datetime import datetime
# from ckeditor.fields import 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20 , blank=False , null=False , )
    cover = models.FileField(upload_to='static/files/category_cover/' , null=False , blank=False)
    color = models.CharField(max_length=20,default='white')
    post_color = models.CharField(max_length=20 , default='white')


    def __str__(self) :
        return self.name

    class Meta :
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        



class Post(models.Model):
    title = models.CharField(max_length= 50 , null = False , blank = False)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True)
    cover = models.FileField(upload_to= 'static/files/post_cover/' , null = False , blank = False) 
    description = models.CharField(max_length= 300 , blank = False  , null = False)
    publish_at = models.DateField(default=datetime.now() , blank=False)
    event_at = models.DateField(blank=False)
    place = models.CharField(max_length=50, blank=False , null= False)

    def __str__(self) :
        return self.title

    class Meta :
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

