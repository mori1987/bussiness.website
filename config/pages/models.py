from django.db import models


class contact(models.Model):
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone= models.IntegerField(null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    date_time=  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



class About_us(models.Model):
    title = models.CharField(max_length=200)
    text =  models.TextField()
    image = models.ImageField(upload_to ='about/')

    def __str__(self):
        return self.title


