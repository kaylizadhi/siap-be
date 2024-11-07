from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import DaftarAkun
from .forms import FormBuatAkun  
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

# List all accounts (GET)
@csrf_exempt
def akun_list(request):
    if request.method == 'GET':
        accounts = DaftarAkun.objects.filter(is_deleted=False).values('username', 'nama', 'email', 'role')
        accounts_list = list(accounts)
        return JsonResponse(accounts_list, safe=False)

# Get an existing account (GET)
@csrf_exempt
def get_existing_account(request):
    if request.method == 'GET':
        # Fetch all accounts that were created in a different page
        # Modify the filter criteria as needed if you want specific accounts
        accounts = DaftarAkun.objects.filter(is_deleted=False).values('username', 'nama', 'email', 'role')
        accounts_list = list(accounts)
        
        # Return the existing accounts in JSON format
        return JsonResponse(accounts_list, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

# Soft delete an account (DELETE)
@csrf_exempt
def akun_delete(request, id):
    akun = get_object_or_404(DaftarAkun, id=id)
    if request.method == 'DELETE':
        akun.is_deleted = True 
        akun.save()
        return JsonResponse({'message': 'Account deleted successfully'}, status=204)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Search accounts
@csrf_exempt
def search_akun(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = DaftarAkun.objects.filter(
            Q(username__icontains=query) |
            Q(nama__icontains=query) |
            Q(role__icontains=query),
            is_deleted=False
        )

    data = [
        {
            'username': akun.username,
            'nama': akun.nama,
            'email': akun.email,
            'role': akun.role,
        }
        for akun in results
    ]

    return JsonResponse(data, safe=False)
