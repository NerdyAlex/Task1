from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pin(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    