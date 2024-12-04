from rest_framework import serializers
from .models import Survei

class SurveiPost(serializers.ModelSerializer):
    class Meta:
        model = Survei
        fields = '__all__'
