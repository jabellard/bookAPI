from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(User, related_name='authors', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, related_name='publishers', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % (self.name)


class Genre(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='genres', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % (self.name)


class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books', null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='books', null=True,
                              blank=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Publisher, related_name='books',
                                  null=True, blank=True, on_delete=models.SET_NULL)
    date_published = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%s' % (self.title)
