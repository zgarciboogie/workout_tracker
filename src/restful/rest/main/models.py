from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=256)


class FeatureValue(models.Model):
    CHOICES = (
        ('number', 'int'),
        ('text', 'str')
    )
    value = models.CharField(max_length=1000)
    value_type = models.CharField(max_length=256, choices=CHOICES, default='text')


class Feature(models.Model):
    name = models.CharField(max_length=256)
    value = models.ManyToManyField(FeatureValue)


class Exercise(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    feature = models.ManyToManyField(Feature)

