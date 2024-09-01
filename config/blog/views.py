from typing import Any
from django.shortcuts import render , get_object_or_404
from django.views import generic
from . models import Blog , Comment
from . forms import CommentForm
from django.urls import reverse


class BlogListView(generic.ListView):
    model = Blog
    template_name= 'blog/blog_listview.html'
    context_object_name= 'blogs'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name='blog/blog_detailview.html'
    
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['commentform'] = CommentForm()
        return context

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.kwargs['blog_id']})
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        blog_id = int(self.kwargs['blog_id'])
        blog = get_object_or_404(Blog, id=blog_id)
        obj.blog = blog
        obj.save()
        return super().form_valid(form)
                                                                                                                                                                                                     








