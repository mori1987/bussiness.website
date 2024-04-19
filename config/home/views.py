from django.shortcuts import render
from django.views import View
from blog.models import Blog
from pages.forms import ContactCreationForm
from django.views.generic import CreateView
from pages.models import contact
from django.urls import reverse_lazy

class HomeView(View):
    def get(self,request):
        last_three_post= Blog.objects.order_by('date_created')[:3]
        return render(request,'home/index.html',{'last_three_post':last_three_post})
        
    def post(self,request):
        return render(request,'home/index.html')




class ContactHomeView(CreateView):
    model = contact
    form_class = ContactCreationForm
    template_name= 'home/index.html'
    success_url=reverse_lazy('home:home')
    
    

