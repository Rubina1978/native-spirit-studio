from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Reflection(models.Model):
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100)

    happy_moment = models.TextField()
    challenge = models.TextField()
    gratitude = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_on}"
