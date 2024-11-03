from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import TrackerSurvei
from .serializers import TrackerSurveiSerializer
import logging

logger = logging.getLogger(__name__)

class RolePermission:
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def has_permission(self, request, view):
        if not hasattr(request.user, 'role'):
            return False
        return request.user.role in self.allowed_roles

def validate_role_fields(user_role, data):
    """Validate that the user can only modify fields within their role."""
    role_field_mapping = {
        'Administrasi': {
            'buat_kontrak', 'buat_invoice', 
            'pembayaran_lunas', 'pembuatan_kwitansi'
        },
        'Logistik': {
            'terima_request_souvenir', 
            'ambil_souvenir'
        },
        'Pengendali Mutu': {
            'terima_info_survei', 'lakukan_survei',
            'pantau_responden', 'pantau_data_cleaning'
        }
    }

    if user_role not in role_field_mapping:
        raise ValidationError(f"User role '{user_role}' does not have permission to modify any fields")

    allowed_fields = role_field_mapping.get(user_role, set())
    unauthorized_fields = set(data.keys()) - allowed_fields
    if unauthorized_fields:
        raise ValidationError(
            f"User with role '{user_role}' cannot modify these fields: {', '.join(unauthorized_fields)}"
        )

def safe_update_tracker(tracker, user_role, update_data):
    """Safely update tracker with validation and error handling."""
    try:
        validate_role_fields(user_role, update_data)
        
        current_state = {
            field: getattr(tracker, field) 
            for field in update_data.keys()
        }
        
        for field, value in update_data.items():
            setattr(tracker, field, value)
            
        tracker.full_clean()
        tracker.save()
        
        return None
        
    except ValidationError as e:
        for field, value in current_state.items():
            setattr(tracker, field, value)
        
        if hasattr(e, 'message_dict'):
            return e.message_dict
        return {'error': str(e)}
        
    except Exception as e:
        for field, value in current_state.items():
            setattr(tracker, field, value)
            
        logger.error(f"Error updating tracker: {str(e)}")
        return {'error': 'An unexpected error occurred'}

def handle_tracker_update(request, survei_id, allowed_roles):
    """Helper function to handle tracker updates"""
    try:
        role_permission = RolePermission(allowed_roles)
        if not role_permission.has_permission(request, None):
            return Response(
                {"error": f"Access denied. Required roles: {', '.join(allowed_roles)}"},
                status=status.HTTP_403_FORBIDDEN
            )

        tracker = get_object_or_404(TrackerSurvei, survei_id=survei_id)
        error = safe_update_tracker(tracker, request.user.role, request.data)
        
        if error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = TrackerSurveiSerializer(tracker)
        return Response(serializer.data)
        
    except Exception as e:
        logger.error(f"Error updating tracker status: {str(e)}")
        return Response(
            {'error': 'An unexpected error occurred while updating the tracker'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tracker_detail(request, survei_id):
    try:
        tracker = get_object_or_404(TrackerSurvei, survei_id=survei_id)
        serializer = TrackerSurveiSerializer(tracker)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Error fetching tracker detail: {str(e)}")
        return Response(
            {'error': 'Failed to fetch tracker details'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_administrasi_status(request, survei_id):
    """Update tracker status for Administrasi role."""
    return handle_tracker_update(request, survei_id, ['Administrasi'])

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_logistik_status(request, survei_id):
    """Update tracker status for Logistik role."""
    return handle_tracker_update(request, survei_id, ['Logistik'])

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_pengendali_mutu_status(request, survei_id):
    """Update tracker status for Pengendali Mutu role."""
    return handle_tracker_update(request, survei_id, ['Pengendali Mutu'])