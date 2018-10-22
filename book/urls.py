from django.contrib import admin
from rest_framework.documentation import include_docs_urls
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
    url(r'^books/$', BookList.as_view(), name='book_list'),
    url(r'^books/(?P<pk>\d+)/$', BookDetail.as_view(), name='book_detail'),
    url(r'^authors/$', AuthorList.as_view(), name='author_list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author_detail'),
    url(r'^authors/(?P<pk>\d+)/books/$', AuthorBookList.as_view(), name='author_book_list'),
    url(r'^publishers/$', PublisherList.as_view(), name='publisher_list'),
    url(r'^publishers/(?P<pk>\d+)/$', PublisherDetail.as_view(), name='publisher_detail'),
    url(r'^publishers/(?P<pk>\d+)/books/$', PublisherBookList.as_view(), name='publisher_book_list'),
    url(r'^genres/$', GenreList.as_view(), name='genre_list'),
    url(r'^genres/(?P<pk>\d+)/$', GenreDetail.as_view(), name='genre_detail'),
    url(r'^genres/(?P<pk>\d+)/books/$', GenreBookList.as_view(), name='genre_book_list'),
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user_detail'),
    url(r'^users/(?P<pk>\d+)/books$', UserBookList.as_view(), name='user_book_list'),
    url(r'^users/(?P<pk>\d+)/publishers$', UserPublisherList.as_view(), name='user_publisher_list'),
    url(r'^users/(?P<pk>\d+)/authors$', UserAuthorList.as_view(), name='user_author_list'),
    url(r'^users/(?P<pk>\d+)/genres$', UserGenreList.as_view(), name='user_genre_list'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^docs/', include_docs_urls(
        title='Book API',
        description='Book API.',
        public=False
        )),
]
