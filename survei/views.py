from django.shortcuts import render
from django.db.models import Count
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
def get_survei_count_by_region(request):
    ruang_lingkup = request.query_params.get('ruang_lingkup', None)

    REGION_CODE_MAPPING = {
        "Aceh": "ID.AC",
        "Bali": "ID.BA",
        "Banten": "ID.BT",
        "Bengkulu": "ID.BE",
        "Gorontalo": "ID.GO",
        "Jakarta": "ID.JK",
        "Jambi": "ID.JA",
        "Jawa Barat": "ID.JB",
        "Jawa Tengah": "ID.JT",
        "Jawa Timur": "ID.JI",
        "Kalimantan Barat": "ID.KB",
        "Kalimantan Selatan": "ID.KS",
        "Kalimantan Tengah": "ID.KT",
        "Kalimantan Timur": "ID.KI",
        "Kalimantan Utara": "ID.KU",
        "Kepulauan Bangka Belitung": "ID.BB",
        "Kepulauan Riau": "ID.KR",
        "Lampung": "ID.LA",
        "Maluku": "ID.MA",
        "Maluku Utara": "ID.MU",
        "Nusa Tenggara Barat": "ID.NB",
        "Nusa Tenggara Timur": "ID.NT",
        "Papua": "ID.PA",
        "Papua Barat": "ID.PB",
        "Riau": "ID.RI",
        "Sulawesi Barat": "ID.SR",
        "Sulawesi Selatan": "ID.SN",
        "Sulawesi Tengah": "ID.ST",
        "Sulawesi Tenggara": "ID.SG",
        "Sulawesi Utara": "ID.SW",
        "Sumatera Barat": "ID.SB",
        "Sumatera Selatan": "ID.SS",
        "Sumatera Utara": "ID.SU",
        "Yogyakarta": "ID.YO",
    }

    # Daftar kota manual
    CITIES = [
        {"id": "ID.JK.01", "name": "Jakarta Pusat", "province": "Jakarta"},
        {"id": "ID.JK.02", "name": "Jakarta Utara", "province": "Jakarta"},
        {"id": "ID.JK.03", "name": "Jakarta Barat", "province": "Jakarta"},
        {"id": "ID.JK.04", "name": "Jakarta Selatan", "province": "Jakarta"},
        {"id": "ID.JK.05", "name": "Jakarta Timur", "province": "Jakarta"},
        {"id": "ID.JB.01", "name": "Bandung", "province": "Jawa Barat"},
        {"id": "ID.JB.02", "name": "Bogor", "province": "Jawa Barat"},
        {"id": "ID.JB.03", "name": "Bekasi", "province": "Jawa Barat"},
    ]

    if ruang_lingkup == "Nasional":
        data = [{"id": "ID", "value": "Indonesia"}]
        return Response(data, status=status.HTTP_200_OK)

    elif ruang_lingkup == "Provinsi":
        data = [{"id": code, "value": name} for name, code in REGION_CODE_MAPPING.items()]
        return Response(data, status=status.HTTP_200_OK)

    elif ruang_lingkup == "Kota":
        data = [{"id": city["id"], "value": city["name"]} for city in CITIES]
        return Response(data, status=status.HTTP_200_OK)

    else:
        return Response(
            {"error": "Invalid ruang_lingkup parameter"},
            status=status.HTTP_400_BAD_REQUEST,
        )
