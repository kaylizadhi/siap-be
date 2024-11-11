from django.http import JsonResponse
from django.contrib.auth import get_user_model
from accounts.models import User
from django.shortcuts import get_object_or_404
from .models import DaftarAkun
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

User = get_user_model()

# List all accounts (GET)
@csrf_exempt
def akun_list(request):
    if request.method == 'GET':
        accounts = User.objects.values('username', 'first_name', 'last_name', 'email', 'role')
        accounts_list = list(accounts)
        return JsonResponse(accounts_list, safe=False)

# Get an existing account (GET)
@csrf_exempt
def get_existing_account(request):
    if request.method == 'GET':
        # Fetch all accounts that were created in a different page
        # Modify the filter criteria as needed if you want specific accounts
        accounts = User.objects.values('id','username', 'first_name', 'last_name', 'email', 'role')
        accounts_list = list(accounts)
        
        # Return the existing accounts in JSON format
        return JsonResponse(accounts_list, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

# Endpoint delete di backend (hard delete)
@csrf_exempt
def akun_delete(request, id):
    akun = get_object_or_404(User, id=id)
    if request.method == 'DELETE':
        akun = User.objects.get(id=account_id)
        akun.delete()  # Hard delete
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
        results = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(role__icontains=query),

        )

    data = [
        {
            'username': akun.username,
            'first_name': akun.first_name,
            'last_name': akun.last_name,
            'email': akun.email,
            'role': akun.role,
        }
        for akun in results
    ]

    return JsonResponse(data, safe=False)
