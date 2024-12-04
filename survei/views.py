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

# @api_view(['GET'])
# def get_location_data(request):
#     param = request.query_params.get('param', '').lower()

#     if param == 'provinsi':
#         data = [
#             {"id": "Jawa Barat", "name": "Jawa Barat"},
#             {"id": "Jawa Tengah", "name": "Jawa Tengah"},
#             {"id": "Jawa Timur", "name": "Jawa Timur"},
#         ]
#     elif param == 'kabupaten/kota':
#         data = [
#             {"id": "Bandung", "name": "Bandung"},
#             {"id": "Semarang", "name": "Semarang"},
#             {"id": "Surabaya", "name": "Surabaya"},
#         ]
#     else:
#         return Response({"error": "Parameter tidak valid. Gunakan 'provinsi' atau 'kabupaten/kota'."}, status=400)

#     return Response(data)

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
        "Yogyakarta": "ID.YO"
    }

    # counts = (
    #     Survei.objects.values("wilayah_survei")
    #     .annotate(survey_count=Count("id"))
    #     .order_by("wilayah_survei")
    # )

    # data = []
    # for region in counts:
    #     region_code = REGION_CODE_MAPPING.get(region["wilayah_survei"])
    #     if region_code:
    #         data.append({"id": region_code, "value": region["survey_count"]})

    # Fetch all surveys
    surveys = Survei.objects.all()

    # Initialize a dictionary to count surveys per region
    region_counts = {}
    
    if ruang_lingkup == "Nasional":
        nasional_surveys = surveys.filter(ruang_lingkup="Nasional")
        for region_code in REGION_CODE_MAPPING.values():
            region_counts[region_code] = len(nasional_surveys)
    else:
        if ruang_lingkup:
            surveys = surveys.filter(ruang_lingkup=ruang_lingkup)
    # Process each survey
        for survey in surveys:
            province_found = None
            for region_name in survey.wilayah_survei:  # `wilayah_survei` is a list
                if region_name in REGION_CODE_MAPPING:
                    province_found = region_name
                    break
            if province_found:
                region_code = REGION_CODE_MAPPING[province_found]
                region_counts[region_code] = region_counts.get(region_code, 0) + 1

    # Transform the result into a list for the response
    data = [{"id": region, "value": count} for region, count in region_counts.items()]

    return Response(data, status=status.HTTP_200_OK)