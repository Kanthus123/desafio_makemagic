from rest_framework import serializers
from .models import Personagem


class PersonagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = '__all__'
