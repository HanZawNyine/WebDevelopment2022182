from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title
    
    def remove_task_url(self):
        return reverse('todo:delete_tasks',args=[self.created.year,self.created.month,self.created.day,self.slug])
    
    def update_task_url(self):
        return reverse('todo:update_tasks',args=[self.created.year,self.created.month,self.created.day,self.slug])

    