import uuid
from django.db import models

class BuatAkun(models.Model):
    ROLE_CHOICES = [
        ('Eksekutif', 'Eksekutif'),
        ('Admin Sistem', 'Admin Sistem'),
        ('Administrasi', 'Administrasi'), 
        ('Logistik', 'Logistik'),
        ('Pengendali Mutu', 'Pengendali Mutu'),
    ]
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID sebagai user ID unik
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    security_question = models.CharField(max_length=255, default="")
    security_answer = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255)
