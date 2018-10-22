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

    def test_get_authors(self):
        print('getting authors...')
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)

    def test_get_publisers(self):
        print('getting publishers')
        response = self.client.get(reverse('publisher_list'))
        self.assertEqual(response.status_code, 200)

def basic_auth_header(username, password):
    credentials = username + ':' + password
    encoded_credentials = base64.b64encode(bytes(credentials, 'ascii'))
    auth_header = {
        'HTTP_AUTHORIZATION': 'Basic ' + encoded_credentials.decode()
    }
    return auth_header

class TestSetUP(TestCase):
    view = None

    def setUp(self):
        # create regular users
        for i in range(5):
            user = User.objects.create(username='ruser' + str(i))
            user.set_password('1234ab12')
            user.save()

        # create admin users
        for i in range(5):
            user = User.objects.create(username='auser' + str(i), is_superuser=True)
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
                first_name='authorf' + str(i),
                last_name='authorl' + str(i),
                owner=user
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

    def test_get_books(self):
        url = reverse(self.view)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_post_book(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'title': 'book title'
            },
            content_type='application/json',
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 201)

    def test_post_book_bad_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data={
                'title': 'uploaded book',
                'description': 'uploaded book description'
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '1234zzab12')
        )
        self.assertEqual(res.status_code, 401)

    def test_post_book_no_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data={
                'title': 'uploaded book',
                'description': 'uploaded book description'
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)


class BookDetailTest(TestSetUP):
    view = 'book_detail'

    def test_get_book(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_book(self):
        url = reverse(self.view, kwargs={'pk': 88888})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    def test_put_book(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url,
            data={
                'title': 'new title',
                'description': 'new description'
            },
            content_type='application/json',
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 200)

    def test_put_book_bad_auth(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url,
            data={
                'title': 'new title',
                'description': 'new description'
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '1234zzab12')
        )
        self.assertEqual(res.status_code, 401)

    def test_put_book_no_auth(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url,
            data={
                'title': 'new title',
                'description': 'new description'
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_book(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.delete(
            url,
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 204)

    def test_delete_book_bad_auth(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url,
            **basic_auth_header('ruser1', '1234zzab12')
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_book_no_auth(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url
        )
        self.assertEqual(res.status_code, 401)


class AuthorListTest(TestSetUP):
    view = 'author_list'

    def test_get_authors(self):
        url = reverse(self.view)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_post_author(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data={
                'first_name': 'first',
                'last_name': 'last'
            },
            content_type='application/json',
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 201)

    def test_post_author_bad_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data={
                'first_name': 'first',
                'last_name': 'last'
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '1234zzab12')
        )
        self.assertEqual(res.status_code, 401)

    def test_post_author_no_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data={
                'first_name': 'first',
                'last_name': 'last'
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)


class AuthorDetailTest(TestSetUP):
    view = 'author_detail'

    def test_get_author(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_author(self):
        url = reverse(self.view, kwargs={'pk': 88888})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    def test_put_author(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url,
            data={
                'first_name': 'new first name',
                'last_name': 'new last name'
            },
            content_type='application/json',
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 200)

    def test_put_author_bad_auth(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url,
            data={
                'first_name': 'new first name',
                'last_name': 'new last name'
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '1234azzb12')
        )
        self.assertEqual(res.status_code, 401)

    def test_put_author_no_auth(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url,
            data={
                'first_name': 'new first name',
                'last_name': 'new last name'
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_author(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.delete(
            url,
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 204)

    def test_delete_author_bad_auth(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url,
            **basic_auth_header('ruser1', '1234azzb12')
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_author_no_auth(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.put(
            url
        )
        self.assertEqual(res.status_code, 401)


class AuthorBookListTest(TestSetUP):
    view = 'author_book_list'

    def test_get_author_books(self):
        url = reverse(self.view, kwargs={'pk': 1})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_author_books(self):
         url=reverse(self.view, kwargs = {'pk': 88888})
         res=self.client.get(url)
         self.assertEqual(res.status_code, 404)

class PublisherListTest(TestSetUP):
    view = 'publisher_list'

    def test_get_publisers(self):
        url = reverse(self.view)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_post_publisher(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'name': 'publisher'
            },
            **basic_auth_header('auser1', '1234ab12'),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 201)

    def test_post_publisher_bad_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'name': 'publisher'
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '12zz34ab12')
        )
        self.assertEqual(res.status_code, 401)


    def test_post_publisher_no_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'name': 'publisher'
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)

class PublisherDetailTest(TestSetUP):
    view = 'publisher_detail'

    def test_get_publishers(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_publishers(self):
        url = reverse(self.view, kwargs = {'pk': 88888})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    def test_put_publisher(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'name': "pub1"
            },
            content_type='application/json',
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 200)

    def test_put_publisher_bad_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'name': "pub1"
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '1234zzab12')
        )
        self.assertEqual(res.status_code, 401)

    def test_put_publisher_no_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'name': "pub1"
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_publisher(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.delete(
            url,
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 204)

    def test_delete_publisher_bad_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            **basic_auth_header('ruser1', '1234zzab12')
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_publisher_no_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url
        )
        self.assertEqual(res.status_code, 401)

class PublisherBookListTest(TestSetUP):
    view = 'publisher_book_list'

    def test_get_publisher_books(self):
          url = reverse(self.view, kwargs = {'pk': 1})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_publisher_books(self):
          url=reverse(self.view, kwargs = {'pk': 88888})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 404)

class GenreListTest(TestSetUP):
    view = 'genre_list'

    def test_get_genres(self):
        url = reverse(self.view)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_post_genre(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'name': 'test_genre'
            },
            content_type='application/json',
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 201)

    def test_post_genre_bad_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'name': 'test_genre'
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '1234zzab12')
        )
        self.assertEqual(res.status_code, 401)


    def test_post_genre_no_auth(self):
        url = reverse(self.view)

        res = self.client.post(
            url,
            data = {
                'name': 'test_genre'
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)

class GenreDetailTest(TestSetUP):
    view = 'genre_detail'

    def test_get_genre(self):
          url = reverse(self.view, kwargs = {'pk': 1})
          res = self.client.get(url)
          self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_genre(self):
        url = reverse(self.view, kwargs = {'pk': 88888})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    def test_put_genre(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'name': "genre1"
            },
            content_type='application/json',
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 200)

    def test_put_genre_bad_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'name': "genre1"
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '1234azzb12')
        )
        self.assertEqual(res.status_code, 401)

    def test_put_genre_no_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'name': "genre1"
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_genre(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.delete(
            url,
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 204)

    def test_delete_genre_bad_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            **basic_auth_header('ruser1', '1234azzb12')
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_genre_no_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url
        )
        self.assertEqual(res.status_code, 401)

class GenreBookListTest(TestSetUP):
    view = 'genre_book_list'

    def test_get_genre_books(self):
          url = reverse(self.view, kwargs = {'pk': 1})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_genre_books(self):
          url=reverse(self.view, kwargs = {'pk': 88888})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 404)

class UserListTest(TestSetUP):
    view = 'user_list'

    def test_get_users(self):
        url = reverse(self.view)
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

class UserDetailTest(TestSetUP):
    view = 'user_detail'

    def test_get_user(self):
          url = reverse(self.view, kwargs = {'pk': 1})
          res = self.client.get(url)
          self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_user(self):
        url = reverse(self.view, kwargs = {'pk': 88888})
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)

    def test_put_user(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'password': 'newpassword'
            },
            content_type='application/json',
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 200)

    def test_put_user_bad_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'password': 'newpassword'
            },
            content_type='application/json',
            **basic_auth_header('ruser1', '1234azzb12')
        )
        self.assertEqual(res.status_code, 401)

    def test_put_user_no_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            data = {
                'password': 'newpassword'
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_user(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.delete(
            url,
            **basic_auth_header('auser1', '1234ab12')
        )
        self.assertEqual(res.status_code, 204)

    def test_delete_user_bad_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url,
            **basic_auth_header('ruser1', '1234zzab12')
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_user_no_auth(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res = self.client.put(
            url
        )
        self.assertEqual(res.status_code, 401)

class UserBookListTest(TestSetUP):
    view = 'user_book_list'

    def test_get_user_books(self):
          url = reverse(self.view, kwargs = {'pk': 1})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_user_books(self):
          url=reverse(self.view, kwargs = {'pk': 88888})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 404)

class UserPublisherListTest(TestSetUP):
    view = 'user_publisher_list'

    def test_get_user_publishers(self):
          url = reverse(self.view, kwargs = {'pk': 1})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_user_publishers(self):
          url=reverse(self.view, kwargs = {'pk': 88888})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 404)

class UserAuthorListTest(TestSetUP):
    view = 'user_author_list'

    def test_get_user_authors(self):
          url = reverse(self.view, kwargs = {'pk': 1})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_user_authors(self):
          url=reverse(self.view, kwargs = {'pk': 88888})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 404)

class UserGenreListTest(TestSetUP):
    view = 'user_genre_list'

    def test_get_user_genres(self):
        url = reverse(self.view, kwargs = {'pk': 1})
        res=self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_get_nonexistent_user_genres(self):
          url=reverse(self.view, kwargs = {'pk': 88888})
          res=self.client.get(url)
          self.assertEqual(res.status_code, 404)

class RegisterTest(TestSetUP):
    view = 'register'

    def test_post_user(self):
        url = reverse(self.view)
        res = self.client.post(
            url,
            data = {
                'username': 'test_usernamehghjjhjh',
                'password': 'lasthjhhh'
            },
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 201)
