from django.db import models
from django.utils import timezone


class DraftManager(models.Manager):
    def get_queryset(self):
        return super(DraftManager, self).get_queryset().filter(state='draft')


class ConfirmManager(models.Manager):
    def get_queryset(self):
        return super(ConfirmManager, self).get_queryset().filter(state='confirm')


class DoneManager(models.Manager):
    def get_queryset(self):
        return super(DoneManager, self).get_queryset().filter(state='done')


class CancelManager(models.Manager):
    def get_queryset(self):
        return super(CancelManager, self).get_queryset().filter(state='cancel')


# Create your models here.
class HospitalPatient(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    age = models.IntegerField()
    choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    gender = models.CharField(max_length=50, choices=choices, default='other')
    note = models.TextField()
    state_choices = [
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ]
    state = models.CharField(max_length=50, choices=state_choices, default='draft')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    draft = DraftManager()
    confirm = ConfirmManager()
    done = DoneManager()
    cancel = CancelManager()
    objects = models.Manager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name
