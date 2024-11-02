from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from survei.models import Survei

class TrackerSurvei(models.Model):
    STATUS_CHOICES = [
        ('NOT_STARTED', 'Not Started'),
        ('IN_PROGRESS', 'In Progress'),
        ('FINISHED', 'Finished'),
        ('DELAYED', 'Delayed')
    ]

    survei = models.OneToOneField(
        Survei,
        on_delete=models.CASCADE,
        related_name='tracker'
    )

    # Administrasi
    buat_kontrak = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    buat_invoice = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    pembayaran_lunas = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    pembuatan_kwitansi = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    
    # Logistik
    terima_request_souvenir = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    ambil_souvenir = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    
    # Pengendali Mutu
    terima_info_survei = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    lakukan_survei = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    pantau_responden = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )
    pantau_data_cleaning = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NOT_STARTED'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tracker_survei'

    def is_administrasi_finished(self):
        admin_fields = [self.buat_kontrak, self.buat_invoice, 
                       self.pembayaran_lunas, self.pembuatan_kwitansi]
        return all(status == 'FINISHED' for status in admin_fields)
    
    def is_logistik_finished(self):
        logistik_fields = [self.terima_request_souvenir, self.ambil_souvenir]
        return all(status == 'FINISHED' for status in logistik_fields)
    
    def clean(self):
        # Validate Administrasi sequence
        if self.buat_invoice != 'NOT_STARTED' and self.buat_kontrak != 'FINISHED':
            raise ValidationError('Buat Kontrak harus selesai sebelum Buat Invoice dapat dimulai')
        if self.pembayaran_lunas != 'NOT_STARTED' and self.buat_invoice != 'FINISHED':
            raise ValidationError('Buat Invoice harus selesai sebelum Pembayaran Lunas dapat dilakukan')
        if self.pembuatan_kwitansi != 'NOT_STARTED' and self.pembayaran_lunas != 'FINISHED':
            raise ValidationError('Pembayaran Lunas harus selesai sebelum Pembuatan Kwitansi dapat dibuat')

        # Validate Logistik sequence (after Administrasi)
        logistik_fields = {'terima_request_souvenir', 'ambil_souvenir'}
        if any(getattr(self, field) != 'NOT_STARTED' for field in logistik_fields) and not self.is_administrasi_finished():
            raise ValidationError('Semua tugas Administrasi harus selesai sebelum memulai Logistik')

        # Validate Logistik internal sequence
        if self.ambil_souvenir != 'NOT_STARTED' and self.terima_request_souvenir != 'FINISHED':
            raise ValidationError('Menerima request souvenir harus selesai sebelum Mengambil souvenir dapat dimulai')

        # Validate Pengendali Mutu (after Logistik)
        mutu_fields = {'terima_info_survei', 'lakukan_survei', 'pantau_responden', 'pantau_data_cleaning'}
        if any(getattr(self, field) != 'NOT_STARTED' for field in mutu_fields):
            if not self.is_administrasi_finished():
                raise ValidationError('Semua tugas Administrasi harus selesai sebelum memulai Pengendali Mutu')
            if not self.is_logistik_finished():
                raise ValidationError('Semua tugas Logistik harus selesai sebelum memulai Pengendali Mutu')

        # Validate Pengendali Mutu sequence
        if self.lakukan_survei != 'NOT_STARTED' and self.terima_info_survei != 'FINISHED':
            raise ValidationError('Menerima informasi survei harus selesai sebelum Melakukan survei dapat dimulai')
        if self.pantau_responden != 'NOT_STARTED' and self.lakukan_survei != 'FINISHED':
            raise ValidationError('Melakukan survei harus selesai sebelum memantau responden yang sedang mengisi survei di lapangan')
        if self.pantau_data_cleaning != 'NOT_STARTED' and self.pantau_responden != 'FINISHED':
            raise ValidationError('Memantau responden yang sedang mengisi survei di lapangan harus selesai sebelum memantau banyaknya data yang dilakukan data cleaning')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    # Create tracker automatically when survey is created
    @receiver(post_save, sender=Survei)
    def create_tracker(sender, instance, created, **kwargs):
        if created:
            TrackerSurvei.objects.create(survei=instance)
