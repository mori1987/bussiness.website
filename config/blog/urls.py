from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('blog_list/',views.BlogListView.as_view(),name='blog_list'),
    path('blog_detail/<int:pk>/',views.BlogDetailView.as_view(),name='blog_detail'),
    path('comment/<int:blog_id>/',views.CommentCreateView.as_view(), name='comment_create'),
]