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
def show_fin_reports(request):
    c = '매출액', '매출원가', '매출총이익', '판매비와관리비', '영업이익', '기타손익 및 금융손익', '기타수익', '기타비용', '금융수익', '금융비용', '당기순이익'
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    fin_reports_data = FinReports.objects.filter(category__in=c)
    fin_reports_data = FinReportsSerializer(fin_reports_data, many=True).data
    report = {"report": fin_reports_data}
    return JsonResponse(data=report, safe=False)
