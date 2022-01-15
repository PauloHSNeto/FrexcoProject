from uuid import uuid4
from django.db import models

class Region(models.Model):
    name = models.CharField(primary_key=True,   max_length=20)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

