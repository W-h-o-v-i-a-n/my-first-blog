from django.http import HttpResponse


def index(request):
    return HttpResponse('<h3>Прівєт мір!</h3>')
