from uuid import uuid4
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=20)
