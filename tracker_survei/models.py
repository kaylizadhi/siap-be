from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Survey(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="surveys")
    
    def __str__(self):
        return self.name

class SurveyStatus(models.Model):
    survey = models.OneToOneField(Survey, on_delete=models.CASCADE, related_name="status")
    
    # Administrasi Awal
    invoice_sent = models.BooleanField(default=False)
    payment_received = models.BooleanField(default=False)
    dp_invoice_sent = models.BooleanField(default=False)
    contract_signed = models.BooleanField(default=False)

    # Penyusunan & Pelaksanaan Survei
    survey_questions_prepared = models.BooleanField(default=False)

    # Analisis Data & Laporan Survei
    data_analysis_started = models.BooleanField(default=False)
    
    # Administrasi Akhir
    final_administration_completed = models.BooleanField(default=False)

    # Penyerahan Laporan Survei
    report_delivered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Status of {self.survey.name}"
