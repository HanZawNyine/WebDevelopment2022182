from django.contrib import admin
from .models import HospitalPatient


# Register your models here.
@admin.register(HospitalPatient)
class HospitalPatient(admin.ModelAdmin):
    list_display = ('name', 'slug', 'age', 'gender', 'state', 'publish')
    list_filter = ('state', 'publish', 'gender')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('state', 'publish')