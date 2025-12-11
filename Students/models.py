from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="")  
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return  self.task_name
 
