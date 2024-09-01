from django.urls import path
from .views import ContactView,AboutView, services_view, team_view

app_name = 'pages'
urlpatterns = [
    path('contact/',ContactView.as_view(),name='contact'),
    path('about/',AboutView.as_view(),name='about_us'),
    path('service/',services_view,name='service'),
    path('team/',team_view,name='team'),

    
]