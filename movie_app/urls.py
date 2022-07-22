from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/movie/', movie_list_view),
    path('api/v1/director/', director_list_view),
    path('api/v1/review/', review_list_view),

]
