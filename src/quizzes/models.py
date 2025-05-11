from django.db import models
from categories.models import Category, Tag

class Quiz(models.Model):
    """Modelo para los quizzes"""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='quizzes')
    tags = models.ManyToManyField(Tag, related_name='quizzes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(null=True, blank=True, help_text="Duración del quiz en minutos")

    class Meta:
        verbose_name_plural = "quizzes"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Question(models.Model):
    """Modelo para las preguntas dentro de un quiz"""
    QUESTION_TYPES = [
        ('single', 'Opción Múltiple (Selección Única)'),
        ('multiple', 'Opción Múltiple (Selección Múltiple)'),
        ('true_false', 'Verdadero / Falso'),
        ('short_answer', 'Respuesta Corta'),
    ]
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='single')
    correct_answer = models.TextField(blank=True, null=True, help_text="Respuesta correcta para preguntas de respuesta corta") # Nuevo campo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    """Modelo para las opciones de respuesta de una pregunta"""
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
