from django.urls import path
from .views import GenreAPIView,AuthorAPIView,BookAPIView,BookAPI,AuthorAPI,GenreAPI


urlpatterns =[
    path('book/', BookAPI.as_view()),
    path('author/', AuthorAPI.as_view()),
    path('genre/', GenreAPI.as_view()),
    path('book/<int:pk>/',  BookAPIView.as_view()),
    path('author/<int:pk>/', AuthorAPIView.as_view()),
    path('genre/<int:pk>/', GenreAPIView.as_view()),
]