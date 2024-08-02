# Mixins
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters


# Define the BookFilter class
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

# Book views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author', 'published_date']

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

