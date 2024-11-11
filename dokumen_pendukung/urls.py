from django.urls import path
from .views import generate_invoice_dp, generate_invoice_final, download_template_proposal, generate_kwitansi_dp, generate_kwitansi_final

urlpatterns = [
    path('generate_invoice_dp/', generate_invoice_dp, name='generate_invoice_dp'),
    path('generate_invoice_final/', generate_invoice_final, name='generate_invoice_final'),
    path('download_template_proposal/', download_template_proposal, name='download_template_proposal'),
    path('generate-kwitansi-dp/', generate_kwitansi_dp, name='generate_kwitansi_dp'),
    path('generate-kwitansi-final/', generate_kwitansi_final, name='generate_kwitansi_final'),
]