from django.db import models

# Create your models here.
class ZPool(models.Model):
    volume_name = models.CharField(max_length=50)
    #create_time = pub_date = models.DateTimeField('date published')
