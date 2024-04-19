from django.urls import path
from .views import ContactView,AboutView

app_name = 'pages'
urlpatterns = [
    path('contact/',ContactView.as_view(),name='contact'),
    path('about/',AboutView.as_view(),name='about_us')
]