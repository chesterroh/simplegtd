from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# Create your views here.

from django.http import HttpResponse
from .models import Question,Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list' : latest_question_list, }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")
    return render(request,'polls/detail.html',{ 'question': question})

def results(request,question_id):
    return HttpResponse("you're looking at the results of %s" % question_id)

def vote(request,question_id):
    return HttpResponse("you're voting at %s" % question_id)

