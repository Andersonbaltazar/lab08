from rest_framework import serializers
from .models import Serie, Category
from django.contrib.auth.models import User

class SerieSerializer(serializers.ModelSerializer):
    category_description = serializers.SerializerMethodField()

    class Meta:
        model = Serie
        fields ='__all__'

    def get_category_description(self, obj):
        return obj.category.description


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')