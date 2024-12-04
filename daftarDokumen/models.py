from django.db import models

# class DaftarDokumen(models.Model):
#     # kode = models.CharField(max_length=100, unique=True)
#     # survey = models.CharField(max_length=255)
#     # klien = models.CharField(max_length=255)
#     # jenisDokumen = models.CharField(max_length=100)
#     # responden = models.CharField(max_length=255)

#     # def __str__(self):
#     #     return self.username

#     id = models.CharField(max_length=255)  # Non-auto-generated unique ID
#     client_name = models.CharField(max_length=255)
#     survey_name = models.CharField(max_length=255)
#     respondent_count = models.IntegerField()
#     address = models.TextField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     nominal_tertulis = models.TextField()
#     paid_percentage = models.DecimalField(max_digits=5, decimal_places=2)
#     additional_info = models.TextField(blank=True, null=True)
#     date = models.DateField()

#     def __str__(self):
#         return f"{self.client_name} - {self.survey_name}"
