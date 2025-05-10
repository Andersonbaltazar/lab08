from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework import action
from rest_framework import Response

from .models import Quiz, Question, Choice

from .serializers import (
    QuizSerializer, QuizDetailSerializer,
    QuestionSerializer, QuestionDetailSerializer,
    ChoiceSerializer, AnswerSerializer
)
