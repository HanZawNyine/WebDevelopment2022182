from django.db import models

class task(models.Model):
    title = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)