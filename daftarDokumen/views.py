from django.http import JsonResponse
# from django.contrib.auth import get_user_model
from dokumen_pendukung.models import InvoiceDP, InvoiceFinal, KwitansiDP, KwitansiFinal
from django.shortcuts import get_object_or_404
# from .models import DaftarAkun
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db.models.functions import Concat
from urllib.parse import unquote
import json

# List all documents (GET)
@csrf_exempt
def dokumen_list(request):

    # Query InvoiceDP
    invoice_dp = InvoiceDP.objects.filter(is_deleted=False).values(
        'id', 'client_name', 'survey_name', 'doc_type'
    )

    # Query InvoiceFinal
    invoice_final = InvoiceFinal.objects.filter(is_deleted=False).values(
        'id', 'client_name', 'survey_name', 'doc_type'
    )

    # Query KwitansiDP
    kwitansi_dp = KwitansiDP.objects.filter(is_deleted=False).values(
        'id', 'client_name', 'survey_name', 'doc_type'
    )

    # Query KwitansiFinal
    kwitansi_final = KwitansiFinal.objects.filter(is_deleted=False).values(
        'id', 'client_name', 'survey_name', 'doc_type'
    )

    if request.method == 'GET':
        dokumen = invoice_dp.union(invoice_final, kwitansi_dp, kwitansi_final)
        dokumen_list = list(dokumen)
        return JsonResponse(dokumen_list, safe=False)

# # Get an existing account (GET)
# @csrf_exempt
# def get_existing_account(request):
#     if request.method == 'GET':
#         # Fetch all accounts that were created in a different page
#         # Modify the filter criteria as needed if you want specific accounts
#         dokumen = InvoiceDP.objects.filter(is_deleted=False).values('id','username', 'first_name', 'last_name', 'email', 'role')
#         dokumen_list = list(dokumen)
        
#         # Return the existing accounts in JSON format
#         return JsonResponse(dokumen_list, safe=False)
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=405)

# Endpoint delete di backend (soft delete)
@csrf_exempt
def dokumen_delete(request, id):
    decoded_id = unquote(id)
    dokumen = get_object_or_404(InvoiceDP, id=decoded_id)
    if request.method == 'DELETE':
        dokumen.is_deleted =True  # Mark as deleted
        dokumen.save()
        return JsonResponse({'message': 'Document deleted successfully'}, status=204)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Detail view of a document (GET)
@csrf_exempt
def dokumen_detail(request, id):
    decoded_id = unquote(id)
    print(f"Decoded ID: {decoded_id}")

    # Query InvoiceDP
    invoice_dp = InvoiceDP.objects.filter(is_deleted=False, id=decoded_id).values(
        'id', 'survey_name', 'client_name', 'doc_type',
        'respondent_count', 'address', 'amount', 
        'nominal_tertulis', 'paid_percentage', 'additional_info', 'date'
    ).first()

    # Query InvoiceFinal
    invoice_final = InvoiceFinal.objects.filter(is_deleted=False, id=decoded_id).values(
        'id', 'survey_name', 'client_name', 'doc_type',
        'respondent_count', 'address', 'amount', 
        'nominal_tertulis', 'paid_percentage', 'additional_info', 'date'
    ).first()

    # Query KwitansiDP
    kwitansi_dp = KwitansiDP.objects.filter(is_deleted=False, id=decoded_id).values(
        'id', 'survey_name', 'client_name', 'doc_type', 
        'amount', 'nominal_tertulis', 'additional_info', 'date'
    ).first()

    # Query KwitansiFinal
    kwitansi_final = KwitansiFinal.objects.filter(is_deleted=False, id=decoded_id).values(
        'id', 'survey_name', 'client_name', 'doc_type', 
        'amount', 'nominal_tertulis', 'additional_info', 'date'
    ).first()

    if request.method == 'GET':
        dokumen = invoice_dp or invoice_final or kwitansi_dp or kwitansi_final
        if dokumen:
            return JsonResponse(dokumen, safe=False)
        else:
            return JsonResponse({'error': 'Document not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


# Search documents
@csrf_exempt
def search_dokumen(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        # Query InvoiceDP
        invoice_dp_results = InvoiceDP.objects.filter(
            Q(id__icontains=query) |
            Q(survey_name__icontains=query) |
            Q(client_name__icontains=query) |
            Q(doc_type__icontains=query),
            is_deleted=False
        ).values('id', 'survey_name', 'client_name', 'doc_type')

        # Query InvoiceFinal
        invoice_final_results = InvoiceFinal.objects.filter(
            Q(id__icontains=query) |
            Q(survey_name__icontains=query) |
            Q(client_name__icontains=query) |
            Q(doc_type__icontains=query),
            is_deleted=False
        ).values('id', 'survey_name', 'client_name', 'doc_type')

        # Query KwitansiDP
        kwitansi_dp_results = KwitansiDP.objects.filter(
            Q(id__icontains=query) |
            Q(survey_name__icontains=query) |
            Q(client_name__icontains=query) |
            Q(doc_type__icontains=query),
            is_deleted=False
        ).values('id', 'survey_name', 'client_name', 'doc_type')

    # Combine results using union
    combined_results = invoice_dp_results.union(invoice_final_results, kwitansi_dp_results)

    # Structure the data
    data = [
        {
            'id': dokumen['id'],
            'survey_name': dokumen['survey_name'],
            'client_name': dokumen['client_name'],
            'doc_type': dokumen['doc_type'],
        }
        for dokumen in combined_results
    ]

    return JsonResponse(data, safe=False)
