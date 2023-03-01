from rest_framework import serializers

from ads.models import Ad, Category
from ads.validators import not_false


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[not_false], required=False)

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Ad
        fields = '__all__'


class AdDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
