from django.db import models
from django.urls import reverse

class Job(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    desc = models.TextField()
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("jobs-detail", args=[str(self.id)])
    