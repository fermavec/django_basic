from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("Welcome to Fer Mavec Django's Project")


def detail(response, question_id):
    return HttpResponse(f'You are seeing the {question_id} question')


def results(response, question_id):
    return HttpResponse(f'You are seeing the results for {question_id} question')


def vote(response, question_id):
    return HttpResponse(f'You are voting for {question_id} question')