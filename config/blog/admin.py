from django.contrib import admin
from . models import Blog,Comment


admin.site.register(Blog)

class CommentAdmin(admin.ModelAdmin):
    list_display= ('user','blog','text','date_created')


admin.site.register(Comment,CommentAdmin)
