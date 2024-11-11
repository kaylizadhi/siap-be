from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .models import BuatAkun
import json
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required #untuk verify is it really admin
def check_role_adminsistem(request):
    if request.user.role == 'Admin Sistem':  
        return JsonResponse({'role': 'Admin Sistem'})
    else:
        return JsonResponse({'error': 'User is not an Admin Sistem'}, status=403)

@csrf_exempt
def buat_akun(request):
    if request.method == "GET":
        # Serve role choices to the front end
        roles = [role[0] for role in BuatAkun.ROLE_CHOICES]
        return JsonResponse({"roles": roles}, status=status.HTTP_200_OK)

    if request.method == "POST":
        data = json.loads(request.body)
        
        # Check if required fields are present
        required_fields = ["username", "first_name", "last_name", "email", "role", "password", "security_question", "security_answer"]
        for field in required_fields:
            if field not in data:
                return JsonResponse({"error": f"{field} is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the BuatAkun instance
        try:
            user = User(
                username=data["username"],
                first_name=data["first_name"],
                last_name = data["last_name"],
                email=data["email"],
                role=data["role"],
                security_question=data["security_question"],
                security_answer=data["security_answer"],
                password=data["password"]  # Hash the password
            )
            user.set_password(data["password"])
            user.save()
            return JsonResponse({"message": "Akun telah berhasil dibuat!"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({"error": "Invalid request method."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
