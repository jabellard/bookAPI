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
    """
    get:
    Return a list of all existing Book instances.

    post:
    Create a new Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the specified Book instance.

    put:
    Update the specified Book instance.

    delete:
    Delete the specified Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AuthorList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing Author instances.

    post:
    Create a new Author instance.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the specified Author instance.

    put:
    Update the specified Author instance.

    delete:
    Delete the specified Author instance.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AuthorBookList(generics.RetrieveAPIView):
    """
    get:
    Return a list of all Book instances by the specified author.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorBookSerializer


class PublisherList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing Publisher instances.

    post:
    Create a new Publisher instance.
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the specified Publisher instance.

    put:
    Update the specified Publisher instance.

    delete:
    Delete the specified Publisher instance.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PublisherBookList(generics.RetrieveAPIView):
    """
    get:
    Return a list of all Book instances by the specified publisher.
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherBookSerializer


class GenreList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing Genre instances.

    post:
    Create a new Genre instance.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the specified Genre instance.

    put:
    Update the specified Genre instance.

    delete:
    Delete the specified Genre instance.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class GenreBookList(generics.RetrieveAPIView):
    """
    get:
    Return a list of all Book instances by the specified genre.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreBookSerializer


class UserList(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing User instances.

    post:
    Create a new User instance.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the specified User instance.

    put:
    Update the specified User instance.

    delete:
    Delete the specified User instance.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserBookList(generics.RetrieveAPIView):
    """
    get:
    Return a list of all Book instances created by the specified user.
    """
    queryset = User.objects.all()
    serializer_class = UserBookSerializer


class UserPublisherList(generics.RetrieveAPIView):
    """
    get:
    Return a list of all Publisher instances created by the specified user.
    """

    queryset = User.objects.all()
    serializer_class = UserPublisherSerializer


class UserAuthorList(generics.RetrieveAPIView):
    """
    get:
    Return a list of all Author instances created by the specified user.
    """

    queryset = User.objects.all()
    serializer_class = UserAuthorSerializer


class UserGenreList(generics.RetrieveAPIView):
    """
    get:
    Return a list of all Genre instances created by the specified user.
    """

    queryset = User.objects.all()
    serializer_class = UserGenreSerializer


class Register(generics.CreateAPIView):
    """
    post:
    Create a new User instance.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
