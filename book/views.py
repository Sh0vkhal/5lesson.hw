from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView

# Create your views here.
from .models import Genre,Author,Book
from .serializers import GenreSerializer,AuthorSerializer,BookSerializer


class GenreAPI(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorAPI(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer    


class BookAPI(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 





class GenreAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer    



class BookAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
    