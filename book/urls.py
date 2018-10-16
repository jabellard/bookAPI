from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import BookListCreateAPIView
from .views import BookRetrieveUpdateDestroyAPIView
from .views import AuthorListCreateAPIView
from .views import AuthorRetrieveUpdateDestroyAPIView
from .views import AuthorBookListAPIView
from .views import PublisherListCreateAPIView
from .views import PublisherRetrieveUpdateDestroyAPIView
from .views import GenreListCreateAPIView
from .views import GenreRetrieveUpdateDestroyAPIView
from .views import UserListCreateAPIView


urlpatterns = [
    url(r'^books/$', BookListCreateAPIView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', BookRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^authors/$', AuthorListCreateAPIView.as_view()),
    url(r'^authors/(?P<pk>\d+)/$', AuthorRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^authors/(?P<pk>\d+)/books/$', AuthorBookListAPIView.as_view()),
    url(r'^publishers/$', PublisherListCreateAPIView.as_view()),
    url(r'^publishers/(?P<pk>\d+)/$', PublisherRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^genres/$', GenreListCreateAPIView.as_view()),
    url(r'^genres/(?P<pk>\d+)/$', GenreRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^users/$', UserListCreateAPIView.as_view()),
]
