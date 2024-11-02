from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import TrackerSurvei
from .serializers import TrackerSurveiSerializer

@api_view(['GET'])
def get_tracker_detail(request, survei_id):
    tracker = get_object_or_404(TrackerSurvei, survei_id=survei_id)
    serializer = TrackerSurveiSerializer(tracker)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_tracker_status(request, survei_id):
    tracker = get_object_or_404(TrackerSurvei, survei_id=survei_id)
    
    try:
        # Get current state of the tracker
        current_state = {field: getattr(tracker, field) for field in request.data.keys()}
        
        # Update tracker with new values
        for field, value in request.data.items():
            setattr(tracker, field, value)
            
        # Try to save with validation
        tracker.save()
        
        serializer = TrackerSurveiSerializer(tracker)
        return Response(serializer.data)
        
    except ValidationError as e:
        # Restore previous state if validation fails
        for field, value in current_state.items():
            setattr(tracker, field, value)
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)