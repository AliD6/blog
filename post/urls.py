from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html")),
    path('' , views.indexpage.as_view() ),#, name = indexpage),
    path('map/' , views.Mappage.as_view() ),

]