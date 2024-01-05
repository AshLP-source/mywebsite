from django.contrib import admin
from .models import *

from django.contrib import admin



class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' , 'title')
    list_display_links = ('id', 'name')
    search_fields = ('id','name','title')

admin.site.register(Request, RequestAdmin)