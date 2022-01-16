from rest_framework import serializers
from FrexcoDesafio import models

class DesafioSerializers(serializers.ModelSerializer):
        class Meta:
          model = models.Region
          fields  = "__all__"