from django.db import models
from django.contrib.auth.models import User

class TicketStatus(models.TextChoices):
    start = 'Start'
    in_progress = 'In Progress'
    in_review = 'In Review'
    done = 'done'

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.start)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['complete']