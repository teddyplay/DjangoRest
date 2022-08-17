from movie_app.serializers import DirectorSerializers, MovieSerializersList, ReviewSerializers
from movie_app.models import Director, Movie, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination


class DirectorCreateListAPIVeiw(ListCreateAPIView):
    queryset = Director.objects.get_queryset().order_by('id')
    serializer_class = DirectorSerializers
    pagination_class = PageNumberPagination


class DirectorDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers


class MovieCreateListAPIVeiw(ListCreateAPIView):
    queryset = Director.objects.get_queryset().order_by('id')
    serializer_class = MovieSerializersList
    pagination_class = PageNumberPagination


class MovieDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializersList


class ReviewCreateListAPIVeiw(ListCreateAPIView):
    queryset = Review.objects.get_queryset().order_by('id')
    serializer_class = ReviewSerializers
    pagination_class = PageNumberPagination


class ReviewDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


# @api_view(['GET', 'POST'])
# def Director_Create_ListView(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializers(directors, many=True)
#         return Response(data=serializer.data)
#     elif request.method == 'POST':
#         serializers_ = DirectorValidateSerializer(data=request.data)
#         if not serializers_.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializers_.errors})
#         name = request.data.get('name')
#         director = Director.objects.create(name=name)
#         return Response(data=DirectorSerializers(director).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def DirectorDetailView(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Director not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorSerializers(director)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(data={'massage': 'Director removed!'})
#     else:
#         director.name = request.data.get('name')
#         director.save()
#         return Response(data=DirectorSerializers(director).data)
#
#
# @api_view(['GET', 'POST'])
# def Movie_Create_ListView(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializersList(movies, many=True)
#         return Response(data=serializer.data)
#     elif request.method == 'POST':
#         serializers_ = MovieValidateSerializer(data=request.data)
#         if not serializers_.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializers_.errors})
#         title = request.data.get('title')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         director_id = request.data.get('director_id')
#         movie = Movie.objects.create(title=title, description=description, duration=duration,
#                                      director_id=director_id)
#         return Response(data=MovieSerializersList(movie).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def MovieDetailView(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'error': 'Movie not Found!!!'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = MovieSerializersList(movie)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(data={'massage': 'Movie removed!'})
#     else:
#         movie.title = request.data.get('title')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director_id = request.data.get('director_id')
#         movie.save()
#         return Response(data=MovieSerializersList(movie).data)
#
#
# @api_view(['GET', 'POST'])
# def Review_Create_ListView(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializers(reviews, many=True)
#         return Response(data=serializer.data)
#     elif request.method == 'POST':
#         serializers_ = ReviewValidateSerializer(data=request.data)
#         if not serializers_.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializers_.errors})
#         text = request.data.get('text')
#         movie_id = request.data.get('movie_id')
#         stars = request.data.get('stars')
#         review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
#         return Response(data=ReviewSerializers(review).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def ReviewDetailView(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Product not found'})
#
#     if request == 'GET':
#         serializer = ReviewSerializers(review)
#         return Response(data=serializer.data)
#     elif request == 'DELETE':
#         review.delete()
#         return Response(data={'massage': 'Review removed!'})
#     else:
#         review.text = request.data.get('text')
#         review.movie = request.data.get('movie')
#         review.stars = request.data.get('stars')
#         review.save()
#         return Response(data=ReviewSerializers(review).data)
#
