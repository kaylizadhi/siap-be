from django.urls import path
from .views import generate_invoice_dp, generate_invoice_final, download_template_proposal, upload_template_proposal, download_template_kontrak, upload_template_kontrak

urlpatterns = [
    path('generate_invoice_dp/', generate_invoice_dp, name='generate_invoice_dp'),
    path('generate_invoice_final/', generate_invoice_final, name='generate_invoice_final'),
    path('download_template_proposal/', download_template_proposal, name='download_template_proposal'),
    path('upload_template_proposal/', upload_template_proposal, name='upload_template_proposal'),
    path('download_template_kontrak/', download_template_kontrak, name='download_template_kontrak'),
    path('upload_template_kontrak/', upload_template_kontrak, name='upload_template_kontrak'),
]