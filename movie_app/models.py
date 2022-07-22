from django.db import models


class Director(models.Model):
    name = models.CharField('Имя', max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', max_length=500)
    duration = models.IntegerField('Продолжительность', max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField('Описание', max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text






# Create your models here.
