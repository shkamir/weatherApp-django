from django.contrib import admin

from .models import City
# Register your models here.
class CityManage(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(City, CityManage)