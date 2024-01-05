
from django.db import models


class Request(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name")
    email = models.CharField(max_length=100,verbose_name="Email")
    title = models.CharField(max_length=100,verbose_name="Title")
    description = models.TextField(blank=True , verbose_name="Message")

