from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello Django Study")


def json_test(request):
    return JsonResponse({'test': 'test'})