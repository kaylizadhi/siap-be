from rest_framework import serializers
from .models import Survei
from klien.models import DataKlien

class SurveiGet(serializers.ModelSerializer):
    nama_klien = serializers.CharField(source='klien.nama_perusahaan', read_only=True)

    class Meta:
        model = Survei
        fields = [
            'id',
            'nama_survei',
            'nama_klien',
            'waktu_mulai_survei',
            'waktu_berakhir_survei',
            'harga_survei',
            'ruang_lingkup',
            'ruang_'
            'wilayah_survei',
            'jumlah_responden',
            'tipe_survei'
        ]

class SurveiPost(serializers.ModelSerializer):
    klien_id = serializers.PrimaryKeyRelatedField(
        queryset=DataKlien.objects.all(),
        source='klien',
        write_only=True
    )
    nama_klien = serializers.SerializerMethodField()

    class Meta:
        model = Survei
        fields = (
            "id", "nama_survei", "waktu_mulai_survei",
            "waktu_berakhir_survei", "klien_id", "nama_klien",
            "harga_survei", "ruang_lingkup", "wilayah_survei",
            "jumlah_responden", "tipe_survei"
        )

    def get_nama_klien(self, obj):
        """Return nama_perusahaan from the related DataKlien model as `nama_klien`."""
        return obj.klien.nama_perusahaan if obj.klien else None