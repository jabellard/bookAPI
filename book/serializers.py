from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book
from .models import Author
from .models import Publisher
from .models import Genre


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    genre = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class AuthorBookSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ('books',)


class PublisherSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Publisher
        fields = '__all__'


class PublisherBookSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Publisher
        fields = ('books',)


class GenreSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'


class GenreBookSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Genre
        fields = ('books',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserBookSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('books',)


class UserPublisherSerializer(serializers.ModelSerializer):
    publishers = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('publishers',)


class UserAuthorSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('authors',)


class UserGenreSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('genres',)
