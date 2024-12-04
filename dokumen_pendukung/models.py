from django.db import models

class InvoiceDP(models.Model):
    # Primary key - varchar
    id = models.CharField(max_length=255, primary_key=True)  # Non-auto-generated unique ID
    client_name = models.CharField(max_length=255)
    survey_name = models.CharField(max_length=255)
    respondent_count = models.IntegerField()
    address = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    nominal_tertulis = models.TextField()
    paid_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    additional_info = models.TextField(blank=True, null=True)
    date = models.DateField(max_length=255, default="invoiceDP")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client_name} - {self.survey_name}"

class InvoiceFinal(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    client_name = models.CharField(max_length=255)
    survey_name = models.CharField(max_length=255)
    respondent_count = models.IntegerField()
    address = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    nominal_tertulis = models.TextField()
    paid_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    additional_info = models.TextField(blank=True, null=True)
    date = models.DateField()
    doc_type = models.CharField(max_length=255, default="invoiceFinal")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client_name} - {self.survey_name}"

class KwitansiDP(models.Model):
    # Primary key - varchar
    id = models.CharField(max_length=255, primary_key=True)  # Non-auto-generated unique ID
    # pembayar = models.CharField(max_length=255)
    # tujuan_pembayaran = models.CharField(max_length=500)
    client_name = models.CharField(max_length=255)
    survey_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    nominal_tertulis = models.TextField()
    additional_info = models.TextField(blank=True, null=True)
    date = models.DateField()
    doc_type = models.CharField(max_length=255, default="kwitansiDP")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pembayar} - {self.tujuan_pembayaran}"

class KwitansiFinal(models.Model):
    # Primary key - varchar
    id = models.CharField(max_length=255, primary_key=True)  # Non-auto-generated unique ID
    # pembayar = models.CharField(max_length=255)
    # tujuan_pembayaran = models.CharField(max_length=500)
    client_name = models.CharField(max_length=255)
    survey_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    nominal_tertulis = models.TextField()
    additional_info = models.TextField(blank=True, null=True)
    date = models.DateField()
    doc_type = models.CharField(max_length=255, default="kwitansiFinal")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pembayar} - {self.tujuan_pembayaran}"
