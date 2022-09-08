from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(response):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list,
    })


def detail(response, question_id):
    return HttpResponse(f'You are seeing the {question_id} question')


def results(response, question_id):
    return HttpResponse(f'You are seeing the results for {question_id} question')


def vote(response, question_id):
    return HttpResponse(f'You are voting for {question_id} question')