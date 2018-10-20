from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import BookList
from .views import BookDetail
from .views import AuthorList
from .views import AuthorDetail
from .views import AuthorBookList
from .views import PublisherList
from .views import PublisherDetail
from .views import PublisherBookList
from .views import GenreList
from .views import GenreDetail
from .views import GenreBookList
from .views import UserList
from .views import UserDetail
from .views import UserBookList
from .views import UserPublisherList
from .views import UserAuthorList
from .views import UserGenreList
from .views import Register


urlpatterns = [
    url(r'^books/$', BookList.as_view()),
    url(r'^books/(?P<pk>\d+)/$', BookDetail.as_view()),
    url(r'^authors/$', AuthorList.as_view()),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetail.as_view()),
    url(r'^authors/(?P<pk>\d+)/books/$', AuthorBookList.as_view()),
    url(r'^publishers/$', PublisherList.as_view()),
    url(r'^publishers/(?P<pk>\d+)/$', PublisherDetail.as_view()),
    url(r'^publishers/(?P<pk>\d+)/books/$', PublisherBookList.as_view()),
    url(r'^genres/$', GenreList.as_view()),
    url(r'^genres/(?P<pk>\d+)/$', GenreDetail.as_view()),
    url(r'^genres/(?P<pk>\d+)/books/$', GenreBookList.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view()),
    url(r'^users/(?P<pk>\d+)/books$', UserBookList.as_view()),
    url(r'^users/(?P<pk>\d+)/publishers$', UserPublisherList.as_view()),
    url(r'^users/(?P<pk>\d+)/authors$', UserAuthorList.as_view()),
    url(r'^users/(?P<pk>\d+)/genres$', UserGenreList.as_view()),
    url(r'^register/$', Register.as_view()),
]
