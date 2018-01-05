from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h3>Прівєт мір!</h3>')


def post_list(request):
    return render(request, 'blog/post_list.html', {})
