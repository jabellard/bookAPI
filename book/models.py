from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Publisher(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    authors = models.ManyToManyField(Author, related_name='books', null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='books', null=True,
                              blank=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Publisher, related_name='books',
                                  null=True, blank=True, on_delete=models.SET_NULL)
    date_published = models.DateField()

    def __str__(self):
        return self.title
