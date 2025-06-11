from rest_framework import serializers
from .models import Serie, Category

class SerieSerializer(serializers.ModelSerializer):
    category_description = serializers.SerializerMethodField()

    class Meta:
        model = Serie
        fields = ['id', 'name', 'release_date', 'rating', 'image', 'category_description']

    def get_category_description(self, obj):
        return obj.category.description if obj.category else None


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'description')
    
