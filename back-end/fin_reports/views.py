from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from fin_reports.models import FinReports
from fin_reports.models_data import DbUploader
from fin_reports.serializers import FinReportsSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def pre_process(request):
    DbUploader().pre_process()
    return JsonResponse({'preprocessing': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    DbUploader().insert_data()
    return JsonResponse({'Product Upload': 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def send_reports(request):
    try:
        new = request.data
        f = FinReports
        report = FinReports.objects.all().filter(id=new['writen']).values()[0]
        f.id = report['category']
        return JsonResponse({'게시판': f"{f.id}"})
    except:
        return JsonResponse({'board': 'fail'})


# @api_view(['POST'])
# @parser_classes([JSONParser])
# def cases_points(request):
#     current_geo = request.data
#     cases_points = Map.objects.raw('SELECT *, (6371*acos(cos(radians(%s))*cos(radians(latitude))*cos(radians(longitude)'
#                                              '-radians(%s))+sin(radians(%s))*sin(radians(latitude)))) '
#                                              'AS distance FROM maps WHERE type="cases" HAVING distance < 2 and date(meta) > date(subdate(now(), INTERVAL 1 YEAR))',
#                                              [current_geo["latitude"], current_geo["longitude"], current_geo["latitude"]])
#     serializer = MapSerializer(cases_points, many=True)
#     return JsonResponse(data=serializer.data, safe=False)
#
#
# @api_view(['POST'])
# @parser_classes([JSONParser])
# def chat_answer(request):
#     # print('############ 4 ##########')
#     query = request.data['query']
#     label = (IntentChat().predictModel(query))
#     answer = Chatbot.objects.filter(label=label).values('answer').order_by('?').first()
#     answer['queryid'] = request.data['key']
#     return JsonResponse(data=answer, safe=False)