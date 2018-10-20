from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .models import Author
from .models import Publisher
from .models import Genre
from django.contrib.auth.models import User
from .serializers import BookSerializer
from .serializers import AuthorSerializer
from .serializers import AuthorBookSerializer
from .serializers import PublisherSerializer
from .serializers import PublisherBookSerializer
from .serializers import GenreSerializer
from .serializers import GenreBookSerializer
from .serializers import UserSerializer
from .serializers import UserBookSerializer
from .serializers import UserPublisherSerializer
from .serializers import UserAuthorSerializer
from .serializers import UserGenreSerializer

# Create your views here.


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorBookList(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorBookSerializer


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherBookList(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherBookSerializer


class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreBookList(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreBookSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserBookList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserBookSerializer


class UserPublisherList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPublisherSerializer


class UserAuthorList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAuthorSerializer


class UserGenreList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserGenreSerializer


class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
