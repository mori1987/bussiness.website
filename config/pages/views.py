from django.shortcuts import render
from django.views.generic import CreateView
from . forms import ContactCreationForm
from django.urls import reverse_lazy
from . models import contact,About_us
from django.views import generic



class ContactView(CreateView):
    model= contact
    form_class = ContactCreationForm
    template_name= 'pages/contact.html'
    success_url=reverse_lazy('home:home')
    

class AboutView(generic.ListView):
    model= About_us
    template_name= 'pages/about-us.html'
    context_object_name= 'about'


def services_view(request):
    return render(request, 'pages/services.html')

def team_view(request):
    return render(request, 'pages/team.html')
