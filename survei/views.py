from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Survei
from .serializers import SurveiGet, SurveiPost
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

class SurveiPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100  

@api_view(['GET'])
def get_list_survei(request):
    paginator = SurveiPagination()
    survei = Survei.objects.all()
    result_page = paginator.paginate_queryset(survei, request)
    serializer = SurveiPost(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def get_survei_detail(request, id):
    try:
        survei = Survei.objects.get(id=id)
    except Survei.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SurveiPost(survei)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_survei(request):
    serializer = SurveiPost(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_survei(request, id):
    try:
        survei = Survei.objects.get(id=id)
    except Survei.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SurveiPost(survei, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_survei(request, id):
    try:
        survei = Survei.objects.get(id=id)
    except Survei.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    survei.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_location_data(request):
    param = request.query_params.get('param', '').lower()

    if param == 'provinsi':
        data = [
        {"id": "Jawa Barat", "name": "Jawa Barat"},
        {"id": "Jawa Tengah", "name": "Jawa Tengah"},
        {"id": "Jawa Timur", "name": "Jawa Timur"},
        {"id": "DKI Jakarta", "name": "DKI Jakarta"},
        {"id": "Banten", "name": "Banten"},
        {"id": "DI Yogyakarta", "name": "DI Yogyakarta"},
        {"id": "Aceh", "name": "Aceh"},
        {"id": "Sumatera Utara", "name": "Sumatera Utara"},
        {"id": "Sumatera Barat", "name": "Sumatera Barat"},
        {"id": "Riau", "name": "Riau"},
        {"id": "Kepulauan Riau", "name": "Kepulauan Riau"},
        {"id": "Jambi", "name": "Jambi"},
        {"id": "Sumatera Selatan", "name": "Sumatera Selatan"},
        {"id": "Bangka Belitung", "name": "Bangka Belitung"},
        {"id": "Bengkulu", "name": "Bengkulu"},
        {"id": "Lampung", "name": "Lampung"},
        {"id": "Kalimantan Barat", "name": "Kalimantan Barat"},
        {"id": "Kalimantan Tengah", "name": "Kalimantan Tengah"},
        {"id": "Kalimantan Selatan", "name": "Kalimantan Selatan"},
        {"id": "Kalimantan Timur", "name": "Kalimantan Timur"},
        {"id": "Kalimantan Utara", "name": "Kalimantan Utara"},
        {"id": "Sulawesi Utara", "name": "Sulawesi Utara"},
        {"id": "Sulawesi Tengah", "name": "Sulawesi Tengah"},
        {"id": "Sulawesi Selatan", "name": "Sulawesi Selatan"},
        {"id": "Sulawesi Tenggara", "name": "Sulawesi Tenggara"},
        {"id": "Sulawesi Barat", "name": "Sulawesi Barat"},
        {"id": "Gorontalo", "name": "Gorontalo"},
        {"id": "Bali", "name": "Bali"},
        {"id": "Nusa Tenggara Barat", "name": "Nusa Tenggara Barat"},
        {"id": "Nusa Tenggara Timur", "name": "Nusa Tenggara Timur"},
        {"id": "Maluku", "name": "Maluku"},
        {"id": "Maluku Utara", "name": "Maluku Utara"},
        {"id": "Papua", "name": "Papua"},
        {"id": "Papua Barat", "name": "Papua Barat"},
        {"id": "Papua Tengah", "name": "Papua Tengah"},
        {"id": "Papua Selatan", "name": "Papua Selatan"},
        {"id": "Papua Pegunungan", "name": "Papua Pegunungan"},
    ]
    elif param == 'kota':
        data = [
        # Aceh
        {"id": "Banda Aceh", "name": "Banda Aceh"},
        {"id": "Langsa", "name": "Langsa"},
        {"id": "Lhokseumawe", "name": "Lhokseumawe"},
        {"id": "Sabang", "name": "Sabang"},
        {"id": "Subulussalam", "name": "Subulussalam"},
        
        # Sumatera Utara
        {"id": "Medan", "name": "Medan"},
        {"id": "Binjai", "name": "Binjai"},
        {"id": "Pematangsiantar", "name": "Pematangsiantar"},
        {"id": "Tanjungbalai", "name": "Tanjungbalai"},
        {"id": "Tebing Tinggi", "name": "Tebing Tinggi"},
        {"id": "Gunungsitoli", "name": "Gunungsitoli"},
        
        # Sumatera Barat
        {"id": "Padang", "name": "Padang"},
        {"id": "Bukittinggi", "name": "Bukittinggi"},
        {"id": "Padangpanjang", "name": "Padangpanjang"},
        {"id": "Pariaman", "name": "Pariaman"},
        {"id": "Payakumbuh", "name": "Payakumbuh"},
        {"id": "Sawahlunto", "name": "Sawahlunto"},
        {"id": "Solok", "name": "Solok"},
        
        # Riau
        {"id": "Pekanbaru", "name": "Pekanbaru"},
        {"id": "Dumai", "name": "Dumai"},
        
        # Kepulauan Riau
        {"id": "Batam", "name": "Batam"},
        {"id": "Tanjung Pinang", "name": "Tanjung Pinang"},
        
        # Jambi
        {"id": "Jambi", "name": "Jambi"},
        {"id": "Sungai Penuh", "name": "Sungai Penuh"},
        
        # Sumatera Selatan
        {"id": "Palembang", "name": "Palembang"},
        {"id": "Lubuklinggau", "name": "Lubuklinggau"},
        {"id": "Pagar Alam", "name": "Pagar Alam"},
        {"id": "Prabumulih", "name": "Prabumulih"},
        
        # Lampung
        {"id": "Bandar Lampung", "name": "Bandar Lampung"},
        {"id": "Metro", "name": "Metro"},
        
        # Bengkulu
        {"id": "Bengkulu", "name": "Bengkulu"},
        
        # Bangka Belitung
        {"id": "Pangkal Pinang", "name": "Pangkal Pinang"},
        
        # Kepulauan Riau
        {"id": "Batam", "name": "Batam"},
        {"id": "Tanjung Pinang", "name": "Tanjung Pinang"},
        
        # DKI Jakarta
        {"id": "Jakarta Utara", "name": "Jakarta Utara"},
        {"id": "Jakarta Barat", "name": "Jakarta Barat"},
        {"id": "Jakarta Selatan", "name": "Jakarta Selatan"},
        {"id": "Jakarta Timur", "name": "Jakarta Timur"},
        {"id": "Jakarta Pusat", "name": "Jakarta Pusat"},
        
        # Jawa Barat
        {"id": "Bandung", "name": "Bandung"},
        {"id": "Bekasi", "name": "Bekasi"},
        {"id": "Bogor", "name": "Bogor"},
        {"id": "Cimahi", "name": "Cimahi"},
        {"id": "Cirebon", "name": "Cirebon"},
        {"id": "Depok", "name": "Depok"},
        {"id": "Sukabumi", "name": "Sukabumi"},
        {"id": "Tasikmalaya", "name": "Tasikmalaya"},
        
        # Jawa Tengah
        {"id": "Semarang", "name": "Semarang"},
        {"id": "Magelang", "name": "Magelang"},
        {"id": "Surakarta", "name": "Surakarta"},
        {"id": "Salatiga", "name": "Salatiga"},
        
        # Jawa Timur
        {"id": "Surabaya", "name": "Surabaya"},
        {"id": "Malang", "name": "Malang"},
        {"id": "Kediri", "name": "Kediri"},
        {"id": "Blitar", "name": "Blitar"},
        {"id": "Madiun", "name": "Madiun"},
        {"id": "Probolinggo", "name": "Probolinggo"},
        {"id": "Pasuruan", "name": "Pasuruan"},
        
        # DI Yogyakarta
        {"id": "Yogyakarta", "name": "Yogyakarta"},
        
        # Bali
        {"id": "Denpasar", "name": "Denpasar"},
        
        # Kalimantan Barat
        {"id": "Pontianak", "name": "Pontianak"},
        {"id": "Singkawang", "name": "Singkawang"},
        
        # Kalimantan Timur
        {"id": "Balikpapan", "name": "Balikpapan"},
        {"id": "Samarinda", "name": "Samarinda"},
        {"id": "Bontang", "name": "Bontang"},
        
        # Sulawesi Selatan
        {"id": "Makassar", "name": "Makassar"},
        {"id": "Palopo", "name": "Palopo"},
        {"id": "Parepare", "name": "Parepare"},
        
        # Papua
        {"id": "Jayapura", "name": "Jayapura"},
    ]

    elif param == 'nasional':
        data = [
            {"id":"Indonesia", 'name': 'Indonesia'}
        ]
    else:
        return Response({"error": "Parameter tidak valid. Gunakan 'provinsi' atau 'kota'."}, status=400)

    return Response(data)