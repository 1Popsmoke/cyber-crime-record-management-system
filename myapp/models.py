from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    picture =models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')

    def __str__(self):
        return self.title

