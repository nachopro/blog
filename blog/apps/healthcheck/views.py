from django.http import HttpResponse


def up(request):
    return HttpResponse('', status=200)
