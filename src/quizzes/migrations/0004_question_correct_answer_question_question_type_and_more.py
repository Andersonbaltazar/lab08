# Generated by Django 5.2.1 on 2025-05-11 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_quiz_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.TextField(blank=True, help_text='Respuesta correcta para preguntas de respuesta corta', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('single', 'Opción Múltiple (Selección Única)'), ('multiple', 'Opción Múltiple (Selección Múltiple)'), ('true_false', 'Verdadero / Falso'), ('short_answer', 'Respuesta Corta')], default='single', max_length=20),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='duration',
            field=models.IntegerField(blank=True, help_text='Duración del quiz en minutos', null=True),
        ),
    ]
