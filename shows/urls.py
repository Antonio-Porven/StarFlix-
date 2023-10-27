from django.urls import path, include
#imports views.py into urls.py
from . import views
urlpatterns = [
    path('movielist/', views.movielist, name='movielist'),
    path('moviemovie/<movie_id>', views.moviemovie, name='movie-movie'),
    path('showgenrelist/', views.genrelist, name='showgenrelist'),
    path('moviegenrelist/', views.genrelist, name='moviegenrelist'),
    path('moviegenreresults/', views.moviegenreresults, name='moviegenreresults'),
    path('profilelist/', views.profilelist, name='profilelist'),
    path('userprofile/<int:pk>', views.profile, name='userprofile'),
    path('showlist/', views.showlist, name='showlist'),
    path('showshow/<show_id>', views.showshow, name='show-show'),
    path('results/', views.searchResults, name='searchResults'),
    path('shows/showgenreresults/<int:category_id>/', views.showgenreresults, name='showgenreresults'),
]
