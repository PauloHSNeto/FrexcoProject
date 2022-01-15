from rest_framework import viewsets
from FrexcoDesafio import models
from FrexcoDesafio.api import serializers




class FrexcoDesafioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FrexcoDesafioSerializer
    queryset = models.Fruit.objects.all()
