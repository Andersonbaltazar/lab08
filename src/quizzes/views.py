from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, Choice

from .serializers import (
    QuizSerializer, QuizDetailSerializer,
    QuestionSerializer, QuestionDetailSerializer,
    ChoiceSerializer, AnswerSerializer
)

class QuizViewSet(viewsets.ModelViewSet):
    """ViewSet para el modelo Quiz"""
    queryset = Quiz.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer

    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        """Valida las respuestas para un quiz específico"""
        quiz = self.get_object()
        submitted_answers = request.data.get('answers', [])
        results = []
        score = 0

        for submitted_answer in submitted_answers:
            question_id = submitted_answer.get('question_id')
            choice_id = submitted_answer.get('choice_id')
            short_answer = submitted_answer.get('short_answer')

            try:
                question = Question.objects.get(id=question_id, quiz=quiz)
                question_type = question.question_type
                is_correct = False
                correct_choices = None
                correct_answer_text = None

                if question_type == 'single':
                    try:
                        choice = Choice.objects.get(id=choice_id, question=question)
                        is_correct = choice.is_correct
                        if not is_correct:
                            correct_choice = Choice.objects.filter(question=question, is_correct=True).first()
                            correct_choices = [correct_choice.id] if correct_choice else None
                    except Choice.DoesNotExist:
                        pass

                elif question_type == 'multiple':
                    if choice_id is not None and isinstance(choice_id, list):
                        selected_choices = Choice.objects.filter(id__in=choice_id, question=question)
                        correct_choices_q = Choice.objects.filter(question=question, is_correct=True)
                        correct_choice_ids = set(c.id for c in correct_choices_q)
                        selected_ids = set(c.id for c in selected_choices)
                        is_correct = selected_ids == correct_choice_ids
                        correct_choices = list(correct_choice_ids)
                    else:
                         return Response({"error": "choice_id debe ser una lista para preguntas de selección múltiple"}, status=status.HTTP_400_BAD_REQUEST)

                elif question_type == 'true_false':
                    try:
                        choice = Choice.objects.get(id=choice_id, question=question)
                        is_correct = choice.is_correct
                        if not is_correct:
                            correct_choice = Choice.objects.filter(question=question, is_correct=True).first()
                            correct_choices = [correct_choice.id] if correct_choice else None
                    except Choice.DoesNotExist:
                        pass

                elif question_type == 'short_answer':
                    correct_answer_text = question.correct_answer
                    if correct_answer_text is not None and short_answer is not None:
                        is_correct = short_answer.strip().lower() == correct_answer_text.strip().lower()

                results.append({
                    'question_id': question_id,
                    'correct': is_correct,
                    'correct_choices': correct_choices,
                    'correct_answer': correct_answer_text,
                    'submitted_choice_id': choice_id if question_type in ['single', 'true_false'] else None,
                    'submitted_choice_ids': choice_id if question_type == 'multiple' else None,
                    'submitted_answer': short_answer if question_type == 'short_answer' else None,
                })
                if is_correct:
                    score += 1

            except Question.DoesNotExist:
                results.append({'question_id': question_id, 'error': 'Pregunta no encontrada'})
            except Choice.DoesNotExist:
                results.append({'question_id': question_id, 'error': 'Opción no encontrada'})

        total_questions = quiz.questions.count()
        percentage = (score / total_questions) * 100 if total_questions > 0 else 0

        return Response({
            'quiz_id': quiz.id,
            'score': f"{score}/{total_questions}",
            'percentage': int(percentage),
            'results': results
        })


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet para el modelo Question"""
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        return QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    """ViewSet para el modelo Choice"""
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
