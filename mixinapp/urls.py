from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView
urlpatterns = [
   path('books/', BookListCreateView.as_view(), name='book-list-create'),
   path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]






















# from django.urls import path
# from .views import BookListCreateView, BookRetrieveUpdateDestroyView, RegistrationView, LoginView, LogoutView, StreamPlatformView, WatchListView, ReviewView

# urlpatterns = [
#     path('books/', BookListCreateView.as_view(), name='book-list-create'),
#     path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
#     path('register/', RegistrationView.as_view(), name='registration'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('streamplatforms/', StreamPlatformView.as_view(), name='streamplatform-list'),
#     path('watchlists/', WatchListView.as_view(), name='watchlist-list'),
#     path('reviews/', ReviewView.as_view(), name='review-list'),




