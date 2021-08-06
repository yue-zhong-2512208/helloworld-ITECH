from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
   	path('add_category/', views.add_category, name='add_category'),

   	path('category/<slug:category_name_slug>/add_movie/',
         views.add_movie, name='add_movie'),
   	path('category/movies/<slug:movie_title_slug>/',
         views.show_movie, name='show_movie'),
  	path('movie/', views.all_movies, name='all_movies'),

   	path('category/movies/<slug:article_title_slug>/add_comment',
         views.add_comment, name='add_comment'),
    path('add_comment/', views.add_comment, name='add_comment'),

    path('restricted/', views.restricted, name='restricted'),
    path('search/', views.search, name='search'),
    path('viewMovies/', views.viewMovies, name='viewMovies'),

]
