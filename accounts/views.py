from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from .models import Profile



@api_view(['GET'])
def get_data(request):
    data = {
        "message": "Hello from Django!"
    }
    return Response(data)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        # Generate or get an existing token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        # Return the token to the frontend
        return Response({"token": token.key, "message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged out successfully"}, status=200)

@login_required
def dashboard_view(request):
    # Only logged in users can access this view
    return JsonResponse({"message": "This is the dashboard"})

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def profil_view(request):
    user = request.user
    if request.method == 'GET':
        # Return user profile data
        return Response({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
        })
    
    if request.method == 'PATCH':
        # Update user profile data
        data = request.data
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'email' in data:
            user.email = data['email']
        if 'username' in data:
            user.username = data['username']
        
        user.save()  # Save the updated user information
        return Response({
            'message': 'Profile updated successfully'
        }, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_security_question(request):
    username = request.data.get('username')
    
    # Try to fetch the user by username
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # If user is found, return the security question
    print({user.profile.security_question})
    return Response({'security_question': user.profile.security_question}, status=status.HTTP_200_OK)

@api_view(['POST'])
def verify_security_answer(request):
    username = request.data.get('username')
    security_answer = request.data.get('security_answer')
    new_password = request.data.get('new_password')

    # Fetch user and profile
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    # Check if the security answer matches the one in the profile
    if profile.security_answer.lower() == security_answer.lower():
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Incorrect security answer'}, status=status.HTTP_400_BAD_REQUEST)
    

# View to return CSRF token
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})
