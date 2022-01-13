from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


def test(request):
    return JsonResponse({'test': 'test'})
