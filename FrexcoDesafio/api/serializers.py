from rest_framework import serializers
from FrexcoDesafio import models


class FrexcoDesafioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fruit
        model2 = models.Region
        fields = '__all__'