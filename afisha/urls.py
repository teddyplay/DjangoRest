from django.contrib import admin
from django.urls import path
from movie_app import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/directors/', views.DirectorCreateListAPIVeiw.as_view()),
    path('api/v1/directors/<int:pk>/', views.DirectorDetailUpdateDestroyAPIView.as_view()),

    path('api/v1/movies/', views.MovieCreateListAPIVeiw.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailUpdateDestroyAPIView.as_view()),


    path('api/v1/reviews/', views.ReviewCreateListAPIVeiw.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailUpdateDestroyAPIView.as_view()),

    path('api/v1/register/', user_views.RegisterAPIView.as_view()),
    path('api/v1/login/', user_views.AuthorizationAPIView.as_view())

]