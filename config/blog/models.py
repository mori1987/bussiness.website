from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to ='blog/',null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified= models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse (blog_detail, args=[self.id])



class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text
