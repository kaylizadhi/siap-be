from django.db import models

class DataKlien(models.Model):
    nama_klien = models.CharField(max_length=50)
    nama_perusahaan = models.CharField(max_length=100)
    daerah = models.TextField()
    harga_survei = models.IntegerField()