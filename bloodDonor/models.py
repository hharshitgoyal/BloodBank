from django.db import models

# Create your models here.
class DonorDetail(models.Model):
    class Meta:
        db_table = 'DonorDetail'

    bloodGroup = models.CharField(max_length=3)
    location = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=10, unique=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
