from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    time=models.CharField(default='00:00:00',max_length=100)
    def __str__(self):
        return f"{self.title} ({self.date})"