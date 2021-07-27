from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# import numpy as np

# Create your views here.
class indexpage(TemplateView):
    # template_name = 'index.html'

    def get(self, request, *args, **kwargs) :
        category_data = []
        all_category = Category.objects.all()#[:2]

        # print(all_category)

        for category in all_category:
            category_data.append({
                'name' : category.name ,
                'cover' : category.cover.url ,
                'color' : category.color,
                'post_color' : category.post_color,
            }) 
        
         # print(category_data)

        post_data =[]
        all_post = Post.objects.all()
        # print(all_post)
        
        for post in all_post:
            post_data.append({
                'title' : post.title ,
                'cover' : post.cover.url , 
                'description' : post.description,
                'category' : post.category,
            })





        context = {
              'category_data' : category_data,
              'post_data' : post_data,
            }
         #  print(context)
        return render(request , 'index.html' , context)

