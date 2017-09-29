from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World... you're at the polls index")

def detail(request,question_id):
    return HttpResponse("you're looking at question %s" % question_id)

def results(request,question_id):
    return HttpResponse("you're looking at the results of %s" % question_id)

def vote(request,question_id):
    return HttpResponse("you're voting at %s" % question_id)
