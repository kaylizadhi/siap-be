import uuid
from django.db import models

class BuatAkun(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Pengendali Mutu', 'Pengendali Mutu'),
        ('Manager', 'Manager'),  # Add other roles here as needed
    ]
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID sebagai user ID unik
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    password = models.CharField(max_length=255)
