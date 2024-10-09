from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import DataKlien
from .forms import DataKlienForm
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q 
import json


# List all clients (GET)
@csrf_exempt
def klien_list(request):
    if request.method == 'GET':
        kliens = DataKlien.objects.all().values('id', 'nama_klien', 'nama_perusahaan', 'daerah', 'harga_survei')
        kliens_list = list(kliens)
        return JsonResponse(kliens_list, safe=False)

# Create a new client (POST)
@csrf_exempt
def klien_create(request):
    if request.method == 'POST':
        try:
            # Load JSON data from request body
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = DataKlienForm(data)
        if form.is_valid():
            klien = form.save()
            return JsonResponse({
                'id': klien.id,
                'nama_klien': klien.nama_klien,
                'nama_perusahaan': klien.nama_perusahaan,
                'daerah': klien.daerah,
                'harga_survei': klien.harga_survei
            }, status=201)
        return JsonResponse(form.errors, status=400)

# Detail view of a client (GET)
@csrf_exempt
def klien_detail(request, id):
    if request.method == 'GET':
        klien = get_object_or_404(DataKlien, id=id)
        return JsonResponse({
            'id': klien.id,
            'nama_klien': klien.nama_klien,
            'nama_perusahaan': klien.nama_perusahaan,
            'daerah': klien.daerah,
            'harga_survei': klien.harga_survei
        })

# Update client details (PUT)
@csrf_exempt
def klien_update(request, id):
    klien = get_object_or_404(DataKlien, id=id)
    
    if request.method == 'PUT' or request.method == 'POST':  # You can use either PUT or POST
        try:
            # Load JSON data from request body
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        form = DataKlienForm(data, instance=klien)
        
        if form.is_valid():
            klien = form.save()
            return JsonResponse({
                'id': klien.id,
                'nama_klien': klien.nama_klien,
                'nama_perusahaan': klien.nama_perusahaan,
                'daerah': klien.daerah,
                'harga_survei': klien.harga_survei
            }, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    
    # Return error if method is not allowed
    return JsonResponse({"error": "Method not allowed"}, status=405)

# Delete a client (DELETE)
@csrf_exempt
def klien_delete(request, id):
    klien = get_object_or_404(DataKlien, id=id)
    if request.method == 'DELETE':
        klien.delete()
        return JsonResponse({'message': 'Client deleted successfully'}, status=204)
        
@csrf_exempt
def search_klien(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = DataKlien.objects.filter(
            Q(nama_klien__icontains=query) |
            Q(nama_perusahaan__icontains=query) |
            Q(daerah__icontains=query)
        )

    # Membuat response data dalam format JSON
    data = [
        {
            'nama_klien': klien.nama_klien,
            'nama_perusahaan': klien.nama_perusahaan,
            'daerah': klien.daerah,
            'harga_survei': klien.harga_survei,
        }
        for klien in results
    ]

    return JsonResponse(data, safe=False)