from django import forms
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    # __str__() = toString()
    def __str__(self):
        return self.name


class Movie(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    STORY_MAX_LENGTH = 500
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    likes = models.IntegerField(default=0)
    poster = models.ImageField(
        upload_to='poster', blank=True)
    year = models.IntegerField(default=2021)
    story = models.CharField(max_length=STORY_MAX_LENGTH)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    posternum = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def readpage(self):
        self.views = self.views + 1


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class LikeMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Like Movie'

    def __str__(self):
        return self.user.username + 'likes' + self.movie.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comments = models.CharField(max_length=128)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comments
