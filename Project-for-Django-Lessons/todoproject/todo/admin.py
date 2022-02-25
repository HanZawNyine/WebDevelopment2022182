from django.contrib import admin
from .  import models

# Register your models here.
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','slug','created')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created',)
    search_fields = ('title',)
    ordering = ('created',)
