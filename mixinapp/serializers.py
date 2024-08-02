from rest_framework import serializers
from mixinapp.models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


















# class StreamPlatformSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StreamPlatform
#         fields = "__all__"

# class WatchListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WatchList
#         fields = "__all__"

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = "__all__"

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
