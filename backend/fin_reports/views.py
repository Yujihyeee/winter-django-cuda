from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from fin_reports.models import FinReports
from fin_reports.models_data import DbUploader
from fin_reports.models_process import ReportProcess
from fin_reports.serializers import FinReportsSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    DbUploader().insert_data()
    return JsonResponse({'Product Upload': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def show_fin_reports(request):
    c = '매출액', '매출원가', '매출총이익', '판매비와관리비', '지급수수료', '영업이익', '기타손익 및 금융손익', '기타수익', '기타비용', '금융수익', '금융비용', '당기순이익(손실)'
    c1 = '매출액', '매출원가', '매출총이익', '판매비와관리비', '지급수수료', '영업이익', '기타손익 및 금융손익', '기타수익', '기타비용', '금융수익', '금융비용', '당기순이익'
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    fin_reports_2020 = FinReports.objects.filter(year__in=['2020'], category__in=c)
    # fin_reports_2021 = FinReports.objects.filter(year__in=['2021'], category__in=c1)
    fin_reports_data = FinReportsSerializer(fin_reports_2020, many=True).data
    return JsonResponse(data=fin_reports_data, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def fin_reports(request):
    ReportProcess().make_report()
    return JsonResponse({'ReportProcess': 'SUCCESS'})
