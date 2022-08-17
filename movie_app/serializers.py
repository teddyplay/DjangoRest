from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
from .models import Director, Review, Movie


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = 'id name count_movies'.split()


class MovieSerializersDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"


class MovieSerializersList(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    filtered_reviews = serializers.SerializerMethodField()

    class Meta:
        model = models.Movie
        fields = "id title director reviews  filtered_reviews".split()

    def get_filtered_reviews(self, product):
        reviews = product.reviews.filter(stars__gt=2)

        return [{'id': review.id,
                 'text': review.text,
                 'reviews': review.stars} for review in reviews]


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, min_length=5)

    def velidate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f'Director with id={director_id} not found!')
        return director_id


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        if Movie.objects.filter(id=movie_id).count() == 0:
            raise ValidationError(f'Movie with id={movie_id} not found!')
        return movie_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_reviews_id(self, reviews_id):
        if Review.objects.filter(id=reviews_id).count() == 0:
            raise ValidationError(f'Reviews with id={reviews_id} not found!')
        return