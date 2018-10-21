from django.test import TestCase
import base64
from django.urls import reverse
from ..models import Author
from ..models import Publisher
from ..models import Genre
from ..models import Book
from django.contrib.auth.models import User
# Create your tests here.


class Test1(TestCase):
    def setUP(self):
        print('setting up')

    def get_authors(self):
        print('getting authors...')
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)

    def get_publisers(self):
        print('getting publishers')
        response = self.client.get(reverse('publisher_list'))
        self.assertEqual(response.status_code, 2900)


class TestSetUP(TestCase):
    view = None

    def basic_auth_header(username, password):
        auth_header = {
            'HTTP_AUTHORIZATION': 'Basic' + '')
        }
        return auth_header

    def setUp(self):
        # create regular users
        for i in range(5):
            user = User.objects.create(username='ruser' + str(i))
            user.set_password('1234ab12')
            user.save()

        # create admin users
        for i in range(5):
            user = User.objects.create(username='auser' + str(i))
            user.set_password('1234ab12')
            user.save()

        # create authors
        user0 = User.objects.get(username='ruser0')
        user1 = User.objects.get(username='ruser1')
        for i in range(5):
            if i % 2 == 0:
                user = user0
            else:
                user = user1
            author = Author.objects.create(
                first_name = 'authorf' + str(i),
                last_name = 'authorl' + str(i),
                owner = user
            )
            author.save()

        # create publishers
        for i in range(5):
            if i % 2 == 0:
                user = user0
            else:
                user = user1
            publisher = Publisher.objects.create(
                name='publisher' + str(i),
                owner=user
            )
            publisher.save()

        # create genres
        for i in range(5):
            if i % 2 == 0:
                user = user0
            else:
                user = user1
            genre = Genre.objects.create(
                name='genre' + str(i),
                owner=user
            )
            genre.save()

        # create books
        author = Author.objects.get(id=1)
        publisher = Publisher.objects.get(id=1)
        genre = Genre.objects.get(id=1)

        for i in range(10):
            if i % 2 == 0:
                user = user0
            else:
                user = user1
            book = Book.objects.create(
                title='book' + str(i),
                description='book description',
                publisher=publisher,
                owner=user
            )
            book.authors.set([author, ])
            book.save()


class BookListTest(TestSetUP):
    view = 'book_list'

    def get_books(self):
        url = reverse(self.view)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def post_book(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'title': 'uploaded book',
                'description': 'uploaded book description'
            },
            **self.basic_auth_header('test_username', 'test_password')
        )
        self.assertEqual(res.status_code, 200)

    def post_book_bad_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'title': 'uploaded book',
                'description': 'uploaded book description'
            },
            **self.basic_auth_header('test_username', 'test_password')
        )
        self.assertEqual(res.status_code, 401)


    def post_book_no_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'title': 'uploaded book',
                'description': 'uploaded book description'
            }
        )
        self.assertEqual(res.status_code, 401)

class BookDetailTest(TestSetUP):
    view='book_detail'

    def get_book(self):
        url=reverse(self.view, kwargs = {'pk': 1})
        res=self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def get_nonexistent_book(self):
        url=reverse(self.view, kwargs = {'pk': 88888})
        res=self.client.get(url)
        self.assertEqual(res.status_code, 404)


class AuthorListTest(TestSetUP):
    view='author_list'
