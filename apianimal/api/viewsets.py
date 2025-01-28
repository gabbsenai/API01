from rest_framework import viewsets
from apianimal.api import serializers
from apianimal import models

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = models.animal.objects.all()
    serializer_class = serializers.AnimalSerializer