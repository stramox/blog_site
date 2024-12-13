from telnetlib import STATUS

from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (("pub", "Published"), ("drf", "Draft"))


    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)

    def __str__(self):
        return self.title