from rest_framework import serializers
from .models import Survei

class SurveiGet(serializers.ModelSerializer):
    class Meta:
        model = Survei
        fields = ("id","nama_survei","waktu_mulai_survei","waktu_berakhir_survei","nama_klien","harga_survei","ruang_lingkup_survei","wilayah_survei","jumlah_responden","tipe_survei")

class SurveiPost(serializers.ModelSerializer):
    class Meta:
        model = Survei
        fields = ("id","nama_survei","waktu_mulai_survei","waktu_berakhir_survei","nama_klien","harga_survei","ruang_lingkup_survei","wilayah_survei","jumlah_responden","tipe_survei")