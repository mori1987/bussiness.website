from django.contrib import admin
from . models import contact,About_us

@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['username','email',]

@admin.register(About_us)
class AboutAdmin(admin.ModelAdmin):
    list_display=['title','text',]
