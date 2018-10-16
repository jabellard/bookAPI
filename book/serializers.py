from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book
from .models import Author
from .models import Publisher
from .models import Genre


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')


class AuthorBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('books',)


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
