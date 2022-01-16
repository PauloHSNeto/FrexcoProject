from rest_framework import viewsets
from FrexcoDesafio import models
from FrexcoDesafio.api import serializers

class DesafioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DesafioSerializers
    queryset = models.Region.objects.all()