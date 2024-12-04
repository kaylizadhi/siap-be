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
        ]
    elif param == 'kota':
        data = [
            {"id": "Bandung", "name": "Bandung"},
            {"id": "Semarang", "name": "Semarang"},
            {"id": "Surabaya", "name": "Surabaya"},
        ]
    elif param == 'nasional':
        data = [
            {"id":"Indonesia", 'name': 'Indonesia'}
        ]
    else:
        return Response({"error": "Parameter tidak valid. Gunakan 'provinsi' atau 'kabupaten'."}, status=400)

    return Response(data)