from django.contrib import admin
from .models import Realtor
class RealtorAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','hire_date')
    list_display_links=['name']
    list_filter=('name',)
    search_fields=('name','hire_date')
    list_per_page=25
admin.site.register(Realtor,RealtorAdmin)
