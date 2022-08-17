from django.db import models

STARS = (

    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),

)

class Director(models.Model):
    name = models.CharField(max_length=100)

    @property
    def count_movies(self):
        return self.movies.all().count()



    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    duration = models.TimeField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='movies')




    def __str__(self):
        return self.title

    @property
    def rating(self):
        reviews = self.reviews.all()
        count = reviews.count()
        average = 0
        for i in reviews:
            average += i.stars
        try:
            return average / count
        except:
            return 0

    @property
    def filter_reviews(self):
        return [{'id': i.id, 'text': i.text, 'stars': i.stars}
                for i in self.reviews.filter(stars__gt=3)]


class Review(models.Model):
    text = models.TextField(verbose_name='Текст')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=5,)

    def __str__(self):
        return self.movie.title
