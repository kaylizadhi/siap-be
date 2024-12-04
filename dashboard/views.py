from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from tracker_survei.models import TrackerSurvei

@api_view(['GET'])
def get_surveys_by_scope(request, scope):
    paginator = PageNumberPagination()

    # Ensure valid TrackerSurvei objects with related Survei
        # Fetch all TrackerSurvei objects with related Survei
    all_surveys = TrackerSurvei.objects.select_related('survei').all()

    # Manual filtering based on scope
    surveys = []
    for tracker in all_surveys:
        if tracker.survei:
            if scope == 'nasional' and tracker.survei.ruang_lingkup == 'Nasional':
                surveys.append(tracker)
            elif scope == 'provinsi' and tracker.survei.ruang_lingkup == 'Provinsi':
                surveys.append(tracker)
            elif scope == 'kota' and tracker.survei.ruang_lingkup == 'Kota':
                surveys.append(tracker)
            elif scope == 'keseluruhan':
                surveys.append(tracker)

    if not surveys:
        return JsonResponse({'error': 'No surveys found for the given scope'}, status=404)

 


    # Construct the data to return
    data = []
    for tracker in surveys:
        survey = tracker.survei
        survey_data = {
            'id': tracker.id,
            'nama_survei': survey.nama_survei,
            'waktu_mulai_survei': survey.waktu_mulai_survei,
            'waktu_berakhir_survei': survey.waktu_berakhir_survei,
            'klien': survey.klien.nama_perusahaan,
            'harga_survei': survey.harga_survei,
            'ruang_lingkup': survey.ruang_lingkup,
            'wilayah_survei': survey.wilayah_survei,
            'jumlah_responden': survey.jumlah_responden,
            'tipe_survei': survey.tipe_survei,
            'last_status': tracker.last_status,
        }
        data.append(survey_data)

    # Return paginated response
    print(data)
    return Response(data)