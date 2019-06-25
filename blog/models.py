from django.db import models

# Create your models here.
class blog(models.Model):
    title       = models.CharField(max_length=120) # max_length=required
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default='this is cool')