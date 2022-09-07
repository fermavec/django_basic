from pyexpat import model
from django.db import models

class Question(models.Model):
    #id Django sets by default (Autoincrement)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)