from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
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
from .serializers import GenreSerializer
from .serializers import UserSerializer

# Create your views here.


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorBookListAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorBookSerializer


class PublisherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = (BasicAuthentication,)
    #permission_classes = (permissions.IsAuthenticated,)


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
