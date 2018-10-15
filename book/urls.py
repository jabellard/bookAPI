from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import BookListCreateAPIView
from .views import BookRetrieveUpdateDestroyAPIView
from .views import AuthorListCreateAPIView
from .views import AuthorRetrieveUpdateDestroyAPIView
from .views import PublisherListCreateAPIView
from .views import PublisherRetrieveUpdateDestroyAPIView
from .views import GenreListCreateAPIView
from .views import GenreRetrieveUpdateDestroyAPIView


urlpatterns = [
    url(r'^books/$', BookListCreateAPIView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', BookRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^authors/$', AuthorListCreateAPIView.as_view()),
    url(r'^authors/<int:pk>/$', AuthorRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^publishers/$', PublisherListCreateAPIView.as_view()),
    url(r'^publishers/<int:pk>/$', PublisherRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^genres/$', GenreListCreateAPIView.as_view()),
    url(r'^genres/<int:pk>/$', GenreRetrieveUpdateDestroyAPIView.as_view()),
]
