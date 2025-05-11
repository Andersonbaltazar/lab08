from rest_framework import serializers
from .models import Quiz, Question, Choice
from categories.models import Category, Tag
from categories.serializers import CategorySerializer, TagSerializer


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer for the Choice model"""
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for the Question model"""
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text']


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Serializer for Question model with nested choices"""
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'choices']

class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), source='tags', write_only=True
    )

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'category', 'category_id', 'tags', 'tag_ids', 'duration', 'created_at']


class QuizDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'duration', 'created_at', 'category', 'tags', 'questions']

    def get_questions(self, obj):
        questions = obj.questions.all()
        return QuestionDetailSerializer(questions, many=True).data


class AnswerSerializer(serializers.Serializer):
    """Serializer for answer validation"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()