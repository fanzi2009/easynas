from django.db import models

# Create your models here.
class ZPool(models.Model):
    volume_name = models.CharField(max_length=50)
    disks = models.CharField(max_length=50)
