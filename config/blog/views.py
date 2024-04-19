from django.shortcuts import render , get_object_or_404
from django.views import generic
from . models import Blog



class BlogListView(generic.ListView):
    model =Blog
    template_name= 'blog/blog_listview.html'
    context_object_name= 'blogs'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name='blog/blog_detailview.html'
    









