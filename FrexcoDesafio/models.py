from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=20)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

