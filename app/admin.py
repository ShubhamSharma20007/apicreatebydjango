from django.contrib import admin
from .views import Company
# Register your models here.

class CustomView(admin.ModelAdmin):
    list_display= ['name','active']


admin.site.register(Company,CustomView)