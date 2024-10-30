from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .models import BuatAkun
import json

@csrf_exempt
def buat_akun(request):
    if request.method == "GET":
        # Serve role choices to the front end
        roles = [role[0] for role in BuatAkun.ROLE_CHOICES]
        return JsonResponse({"roles": roles}, status=status.HTTP_200_OK)

    if request.method == "POST":
        data = json.loads(request.body)
        
        # Check if required fields are present
        required_fields = ["username", "name", "email", "role", "password"]
        for field in required_fields:
            if field not in data:
                return JsonResponse({"error": f"{field} is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the BuatAkun instance
        try:
            user = BuatAkun(
                username=data["username"],
                name=data["name"],
                email=data["email"],
                role=data["role"],
                password=make_password(data["password"])  # Hash the password
            )
            user.save()
            return JsonResponse({"message": "Akun telah berhasil dibuat!"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({"error": "Invalid request method."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
