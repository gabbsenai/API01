from rest_framework import serializers
from apianimal import models

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.animal
        fields = "__all__"