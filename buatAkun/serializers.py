from rest_framework import serializers
from .models import BuatAkun

class BuatAkunSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuatAkun
        fields = ('username','name', 'email','role','password')
