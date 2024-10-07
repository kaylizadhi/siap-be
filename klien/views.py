from django.shortcuts import render
from .models import DataKlien

# Membuat instance sementara tanpa menyimpan ke database
data_klien = DataKlien(
    nama_klien="John Doe",
    nama_perusahaan="Tech Corp",
    daerah="Jakarta",
    harga_survei=100000
)

# Menampilkan data
print(data_klien.nama_klien)
print(data_klien.nama_perusahaan)
print(data_klien.daerah)
print(data_klien.harga_survei)
