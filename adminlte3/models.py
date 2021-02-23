from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Conference(models.Model):
    name = models.CharField(max_length=30)
    venue = models.CharField(max_length=80)
    details = models.TextField(max_length=30)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    details = RichTextField(blank=True, null=True)
    # zip_code = models.IntegerField(default=92)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name